from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

import tensorflow as tf

from utils.gpt2 import predict_mbti

app = FastAPI()
import json

class Text(BaseModel):
    text : str

@app.get("/api/")
def read_root():
    return {"message": "auto-ta-ml-server"}

@app.post("/api/test")
def test(text:Text):
    return {"message": "text"}

@app.post('/api/predict')
def predict(text:Text):

    mbti_type = ["e_i", "n_s", "f_t", "j_p"]
    result = []
    for x in mbti_type:
        result.append(predict_mbti(x, text.text))
    
    res = {}
    res['data'] = result

    return res
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)