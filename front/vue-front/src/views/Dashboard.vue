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

    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col">
          <success-mission v-bind:propsdata="resultSuccessData"></success-mission>
        </div>
      </div>
      <div class="row mt-5">
        <h1></h1>
      </div>
    </div>
    <div class="row mt-5"></div>
    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col">
          <fail-mission v-bind:failmission="resultfailData"></fail-mission>
        </div>
      </div>
      <div class="row mt-5">
        <h1></h1>
      </div>
       <div class="contatiner">
      <div class="row mt-5">
        <div class="col-md-9"></div>
        <MissionKing v-bind:propsdata="resultDataTemp"></MissionKing>
      </div>
    </div>
    </div>
  </div>
</template>
<script>
// Tables

import MissionTable from "./Dashboard/MissionTable";
import SuccessMission from "./Tables/SuccessMission";
import FailMission from "./Tables/FailMission";
import MissionKing from "./Dashboard/MissionKing";

export default {
  components: {
    MissionTable,
    SuccessMission,
    FailMission,
    MissionKing
  },

  data() {
    return {
      resultData: [["aaa", "bbbb", "ccc", "ddd", "2019-06-21"]],
      resultSuccessData: [["aaa", "bb", "ccc", "ddd", "2019-06-21"]],
      resultfailData: [["aaa", "bb", "ccc", "ddd","2019-06-21"]],
      resultDataTemp: []
    };
  },

  methods: {
    manage: function(index, status) {
      //this.resultData.splice(index, 1);
      this.sendServer(index, status);

      console.log(status);
    },
    modify: function(index, status, modifying_data){
      let currentObj = this;
      this.axios
        .post("/" + status, {
          id: this.resultData[index][0],
          content: modifying_data
        })
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          currentObj.trimResultData();
          currentObj.trimSuccessFailResultData();
        })
        .catch(function(error) {
          console.log("senserver error");
        });
    },
    sendServer: function(index, status) {
      if (status !== "new_mission") {
        let currentObj = this;
        this.axios
          .post("/" + status, {
            id: this.resultData[index][0]
          })
          .then(function(response) {
            currentObj.resultDataTemp = response.data;
            currentObj.trimResultData();
          })
          .catch(function(error) {
            console.log("senserver error");
          });
      } else {
        let currentObj = this;
        this.axios
          .post("/" + status, {
            donatorID: index[0],
            content: index[1]
          })
          .then(function(response) {
            currentObj.resultDataTemp = response.data;
            currentObj.trimResultData();
          })
          .catch(function(error) {
            console.log("senserver error");
          });
      }
      let currentObj = this;
      this.axios
        .post("/" + status, {
          id: this.resultData[index][0]
        })
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          currentObj.trimResultData();
          currentObj.trimSuccessFailResultData();
        })
        .catch(function(error) {
          console.log("senserver error");
        });
    },
    refresh: function() {
      let currentObj = this;
      this.axios
        .post("/get_result")
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          //console.log(currentObj.resultDataTemp)
          currentObj.trimResultData();
        })
        .catch(function() {
          console.log("refresh error");
        });
    },
    setRefresh: function() {
      setInterval(() => {
        this.refresh();
      }, 3000);
    },
    trimResultData: function() {
      this.resultData = [];
      for (var i = 0; i < this.resultDataTemp.length; i++) {
        if (this.resultDataTemp[i][3] == "mission") {
          //this.resultDataTemp.splice(i, 1)
          this.resultData.push(this.resultDataTemp[i]);
          this.resultData[i][4] = this.resultData[i][4].substring(0,10);
        }
      }
      //this.resultData = this.resultDataTemp;
      console.log(this.resultData);
    },
    trimSuccessFailResultData: function() {
      this.resultSuceessData = [];
      this.resultFailData = [];
      for (var i = 0; i < this.resultDataTemp.length; i++) {
        if (this.resultDataTemp[i][3] == "success") {
          this.resultSuccessData.push(this.resultDataTemp[i]);
        } else if (this.resultDataTemp[i][3] == "fail") {
          this.resultFailData.push(this.resultDataTemp[i]);
        }
      }
      //this.resultData = this.resultDataTemp;
      console.log(this.resultData);
    }
  },

  mounted() {
    this.setRefresh();
    console.log("mounted");
  },
  created() {
    this.refresh();
    this.trimSuccessFailResultData();
    console.log(this.resultDataTemp);
  }
};
</script>
<style></style>