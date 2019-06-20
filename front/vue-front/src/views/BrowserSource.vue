<template>
    <div class="align-items-center clear">
      <table class="table tablesorter clear">
        <tr v-for="item in datas" :key="item['donatorID']">
          <td>{{item['content']}}</td>
          <td>{{item['donations']}}</td>
        </tr>
      </table>
    </div>
</template>
<script>
export default {
  data() {
    return {
      resultData: [],
      resultDataTemp: [],
      datas : [
        {"donatorID":"donatorid1", "content":"donatecontent1", "donations":"money1"},
        {"donatorID":"id2", "content":"content2", "donations":"money2"},
        {"donatorID":"looooooooooongid2", "content":"looooooooooooooooongcontent3", "donations":"money3"}]
    }
  },

  methods: {
    refresh: function() {
      let currentObj = this;
      this.axios.post('/get_result')
        .then(function(response) {
          currentObj.resultDataTemp = response.data
          //console.log(currentObj.resultDataTemp)
          currentObj.trimResultData()
        })
        .catch(function() {
          console.log("refresh error");
        });
    },
    setRefresh: function() {
      setInterval(() => {
        this.refresh()
      }, 3000)
    },
    trimResultData: function() {
      this.resultData = []
      for (var i = 0; i < this.resultDataTemp.length; i++) {
        if (this.resultDataTemp[i][3] == "mission") {
          //this.resultDataTemp.splice(i, 1)
          this.resultData.push(this.resultDataTemp[i])
        }
      }
      //this.resultData = this.resultDataTemp;
      console.log(this.resultData)
    }
  },
  mounted() {
    this.setRefresh()
    console.log("mounted");
  }
};
</script>
<style>
.clear {
  background-color: #ffffff;
  background-color: rgba( 255, 255, 255, 0 );
}
.table { 
  background-color: rgba( 255, 255, 255, 0 );
  max-width: 100%; 
} 
.tr { background-color: rgba( 255, 255, 255, 0 ); } 
.td { background-color: rgba( 255, 255, 255, 0 ); } 
</style>
