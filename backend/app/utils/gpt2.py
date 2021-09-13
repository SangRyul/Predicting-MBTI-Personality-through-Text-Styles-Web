import os
import tensorflow as tf
from transformers import TFGPT2Model

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import gluonnlp as nlp
from gluonnlp.data import SentencepieceTokenizer

import pandas as pd

import numpy as np
import re
import asyncio

TOKENIZER_PATH = './utils/gpt_ckpt/gpt2_kor_tokenizer.spiece'

tokenizer = SentencepieceTokenizer(TOKENIZER_PATH)
vocab = nlp.vocab.BERTVocab.from_sentencepiece(TOKENIZER_PATH,
                                               mask_token=None,
                                               sep_token='<unused0>',
                                               cls_token=None,
                                               unknown_token='<unk>',
                                               padding_token='<pad>',
                                               bos_token='<s>',
                                               eos_token='</s>')

BATCH_SIZE = 16
NUM_EPOCHS = 10
VALID_SPLIT = 0.2
SENT_MAX_LEN = 128
CLASSIFIER_TYPE = ""
#각 mbti type에 따라 변화 시킬것 e_i, n_s, f_t, j_p로 바꾸어주면 됌

DATA_IN_PATH = './models'
DATA_OUT_PATH = "./models"

class TFGPT2Classifier(tf.keras.Model):
    def __init__(self, dir_path, num_class):
        super(TFGPT2Classifier, self).__init__()
        
        self.gpt2 = TFGPT2Model.from_pretrained(dir_path)
        self.num_class = num_class
        
        self.dropout = tf.keras.layers.Dropout(self.gpt2.config.summary_first_dropout)
        self.classifier = tf.keras.layers.Dense(self.num_class, 
                                                kernel_initializer=tf.keras.initializers.TruncatedNormal(stddev=self.gpt2.config.initializer_range), 
                                                name="classifier")
        
    def call(self, inputs):
        outputs = self.gpt2(inputs)
        pooled_output = outputs[0][:, -1]

        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        return logits


# print(prediction)
# print(tf.nn.softmax(prediction))
# print(np.argmax(prediction))

# 텍스트 전처리

def clean_text(sent):
    sent_clean = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "", sent)
    return sent_clean

def predict_mbti(mbti_type, user_text):

    CLASSIFIER_TYPE = mbti_type
    BASE_MODEL_PATH = './utils/gpt_ckpt'

    cls_model = TFGPT2Classifier(dir_path=BASE_MODEL_PATH, num_class=2)
    optimizer = tf.keras.optimizers.Adam(learning_rate=6.25e-5)
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')
    #f1-score, AUC-ROC, accuracy
    cls_model.compile(optimizer=optimizer, loss=loss, metrics=[metric])
    # test_data = test_data[:50] # for test

    test_data_sents = []
    test_tokenized_text = vocab[tokenizer(clean_text(user_text))]

    tokens = [vocab[vocab.bos_token]]  
    tokens += pad_sequences([test_tokenized_text], 
                            SENT_MAX_LEN, 
                            value=vocab[vocab.padding_token], 
                            padding='post').tolist()[0] 
    tokens += [vocab[vocab.eos_token]]

    test_data_sents.append(tokens)
    test_data_sents = np.array(test_data_sents, dtype=np.int64)
    model_name = f"{CLASSIFIER_TYPE}"
    checkpoint_path = os.path.join(DATA_OUT_PATH, model_name+'_weights.h5')

    cls_model.load_weights(checkpoint_path, by_name=True, skip_mismatch=True)
    prediction = cls_model.predict(test_data_sents)
    prob_prediction = tf.nn.softmax(prediction)[0].numpy().tolist()
    return {CLASSIFIER_TYPE : prob_prediction}