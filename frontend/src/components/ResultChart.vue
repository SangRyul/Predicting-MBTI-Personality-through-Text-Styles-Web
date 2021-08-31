<template>
  <v-container class="result-container">
  <v-row class="result-container">
      <h1> 당신의 MBTI 결과는 {{ mbtiSignal }} 입니다</h1>
  </v-row>
  <v-row align="center" justify="center">
    <v-col :lg="6" :md="12" :sm="12">
      <GChart
    type="ColumnChart"
    :data="chartData1"
    :options="chartOptions"
  />
    </v-col>
    <v-col :lg="6" :md="12" :sm="12">
      <GChart
    type="ColumnChart"
    :data="chartData2"
    :options="chartOptions"
  />
    </v-col>
    <v-col :lg="6" :md="12" :sm="12">
      <GChart
    type="ColumnChart"
    :data="chartData3"
    :options="chartOptions"
  />
    </v-col>
    <v-col :lg="6" :md="12" :sm="12">
      <GChart
    type="ColumnChart"
    :data="chartData4"
    :options="chartOptions"
  />
    </v-col>
  </v-row>
  </v-container>
</template>

<script>

import { GChart } from 'vue-google-charts'

  export default {
    name: 'ResultChart',
    props : ['mbtidata'],
    components: {
      GChart
    },
    watch:{
      mbti(val, newval){
        this.processData(val)
      }
    },
    computed:{
      mbti(){
        return this.mbtidata
      },
      chartData1(){
        return (
          [
            ['type', 'percentage', {role:'style'}],
            ['E', this.chartNum[0] , 'color : #00ffa6'],
            ['I', this.chartNum[1], 'color : #00ffa6'],
          ]
        )
      },
      chartData2(){
        return (
          [
            ['type', 'percentage',{role:'style'}],
            ['N', this.chartNum[2], 'color:#0088ff'],
            ['S', this.chartNum[3], 'color:#0088ff'],
          ]
        )
      },
      chartData3(){
        return (
          [
            ['type', 'percentage',{role:'style'}],
            ['F', this.chartNum[4], 'color:#bb54c4'],
            ['T', this.chartNum[5], 'color:#bb54c4'],
          ]
        )
      },
      chartData4(){
        return(
        [
          ['type', 'percentage',{role:'style'}],
          ['J', this.chartNum[6],'color:#c4546b'],
          ['P', this.chartNum[7], 'color:#c4546b'],
        ] 
      )
      }
    },
    data: () => ({
      chartOptions: {
        legend: {position: 'none'},
        width : "100%",
        height : "100%",
      },
      chartNum : [50,50,50,50,50,50,50,50],
      mbtiSignal : "",
    }),
    methods : {
      processData(val){

        this.mbtiSignal = ""
        
        this.chartNum = [
          val[0]['e_i'][0], 
          val[0]['e_i'][1],

          val[1]['n_s'][0],
          val[1]['n_s'][1],

          val[2]['f_t'][0],
          val[2]['f_t'][1],

          val[3]['j_p'][0],
          val[3]['j_p'][1]
        ]

        this.mbtiSignal += (this.chartNum[0] > this.chartNum[1] ? 'E' : 'I')
        this.mbtiSignal += (this.chartNum[2] > this.chartNum[3] ? 'N' : 'S')
        this.mbtiSignal += (this.chartNum[4] > this.chartNum[5] ? 'F' : 'T')
        this.mbtiSignal += (this.chartNum[6] > this.chartNum[7] ? 'J' : 'P')
      }
    },
    mounted(){
      
    }
  }
</script>

<style lang="scss" scoped>
.result-container{
  background : white;
  padding : 10px;
  border-radius : 10px;

}
</style>