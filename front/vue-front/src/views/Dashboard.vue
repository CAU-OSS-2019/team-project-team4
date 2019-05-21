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
      /* eslint-disable no-console */
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
        /* eslint-disable */
        .catch(function(error) {
          /* eslint-disable no-console */
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
          /* eslint-disable no-console */
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
    /* eslint-disable no-console */
    console.log("mounted");
  }
};
</script>
<style></style>
