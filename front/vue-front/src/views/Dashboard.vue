<template>
  <div>
    <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8"></base-header>

    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col-xl-8 mb-5 mb-xl-0">
          <page-visits-table v-bind:propsdata="resultData"></page-visits-table>
        </div>
        <div class="col-xl-4">
          <mission-control v-bind:propsdata="resultData" v-on:manage="manage"></mission-control>
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

import PageVisitsTable from "./Dashboard/PageVisitsTable";
import MissionControl from "./Dashboard/MissionControl";

export default {
  components: {
    MissionControl,
    PageVisitsTable
  },

  data() {
    return {
      resultData: [
        ["test1", "testdonate", "구르면 천원 줌", "mission"],
        [
          "test2",
          "ChanghwanJjangJjang",
          "창환이는 똑똑하다 하면 처넌 줌",
          "mission"
        ],
        ["test3", "ChanghwanKingGod", "최창환짱짱맨하면 이마넌줌", "mission"]
      ],
      resultDataTemp: []
    };
  },

  methods: {
    manage: function(index, status) {
      this.resultData.splice(index, 1);
      this.sendServer(index, status);

      console.log(status);
    },
    sendServer: function(index, status) {
      let currentObj = this;
      this.axios
        .post("" + "/" + status, {
          id: this.resultData[index][0]
        })
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          this.trimResultData();
        })
        .catch(function(error) {
          console.log("error");
        });
    },
    refresh: function() {
      let currentObj = this;
      this.axios
        .post("" + "/get_result")
        .then(function(response) {
          currentObj.resultDataTemp = response.data;
          this.trimResultData();
        })
        .catch(function() {
          console.log("error");
        });
    },
    setRefresh: function() {
      setInterval(() => {
        this.refresh();
      }, 3000);
    },
    trimResultData: function() {
      for (var i = 0; i < this.resultData.length; i++) {
        if (this.resultDataTemp[i][3] !== "mission") {
          this.resultDataTemp.splice(i, 1);
        }
      }
      this.resultData = this.resultDataTemp;
    }
  },
  mounted() {
    this.setRefresh();
    console.log("mounted");
  }
};
</script>
<style></style>
