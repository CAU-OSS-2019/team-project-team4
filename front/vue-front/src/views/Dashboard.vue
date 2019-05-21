<template>
  <div>
    <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8"></base-header>

    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col">
          <mission-table v-bind:propsdata="resultData" v-on:manage="manage"></mission-table>
        </div>
      </div>
      <div class="row mt-5">
        <h1></h1>
      </div>
    </div>
  </div>
</template>
<script>
// Tables

import MissionTable from "./Dashboard/MissionTable";

export default {
  components: {
    MissionTable
  },

  data() {
    return {
      resultData: [],
      resultDataTemp: [],
    }
  },

  methods: {
    manage: function(index, status) {
      //this.resultData.splice(index, 1);
      this.sendServer(index, status);

      console.log(status);
    },
    sendServer: function(index, status) {
      let currentObj = this;
      this.axios
        .post("/" + status, {
          id: this.resultData[index][0]
        })
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          currentObj.trimResultData()
        })
        .catch(function(error) {
          console.log("senserver error");
        });
    },
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
<style></style>
