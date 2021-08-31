<template>
  <div class="main-container"> 
    <v-sheet rounded="lg" class="sheet-body">
      <div class="mbti-header"> 
        <h1>당신의 MBTI는 무엇일까요?</h1>
        <h2> 아래의 질문을 통하여 당신의 mbti를 알아보세요</h2>
      </div>
      <hr>
      <div class="mbti-body">
        <div class="question-container">
          <h3>본인의 성격을 간단하게 말해주세요</h3>
              <v-textarea
            outlined
            name="input-7-4"
            label="답변"
            :value="answer1"
          ></v-textarea>
        </div>
      </div>
      <div class="button-container">
            <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="success"
        @click="fetchData()"
      >
        Accept Terms
      </v-btn>
      </div>
    </v-sheet>
    
    <resultchart :mbtidata="mbtidata"></resultchart>
  </div>
</template>

<script>

  import resultchart from '../components/ResultChart.vue'
  export default {
    name: 'Home',

    components: {
      resultchart
    },
    watch: {
      loader () {
        const l = this.loader
        this[l] = !this[l]

        setTimeout(() => (this[l] = false), 3000)

        this.loader = null
      },
    },
    data: () => ({
      loader: null,
      loading : false,
      answer1 : "",
      mbtidata : ""
    }),
    methods : {
      fetchData(){
        this.loading = true
        this.mbtidata = ""
        const baseURI = '/api/predict'
        let postData = {
          text : this.answer1
        }
        this.$http.post(baseURI, postData)
        .then((res) => {
          this.loading = false
          this.mbtidata = res.data.data
          console.log(this.mbtidata)
        })
        .catch((error)=>{
          alert(error)
          this.loading = false
        })
      }
    }
  }
</script>
<style lang="scss" scoped>
.sheet-body{
  margin : 0 0 2rem 0;
  .mbti-header{
    text-align:center;
  }
  hr{
    margin : 2rem 0;
  }
  .mbti-body{
    margin : 1rem;
    .button-container{
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }
}

</style>
