<template>
  <div>
    <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8"></base-header>

    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col-xl-8 mb-5 mb-xl-0">
          <page-visits-table v-bind:propsdata="resultData"></page-visits-table>
        </div>
        <div class="col-xl-4">
          <mission-control v-bind:propsdata="resultData1" v-on:manage="manage"></mission-control>
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
      resultData1: [
        ["test1", "testdonate", "구르면 천원 줌", "mission"],
        [
          "test2",
          "ChanghwanJjangJjang",
          "창환이는 똑똑하다 하면 처넌 줌",
          "mission"
        ],
        ["test3", "ChanghwanKingGod", "최창환짱짱맨하면 이마넌줌", "mission"]
      ]
    };
  },

  methods: {
    manage: function(index, status) {
      this.resultData.splice(index, 1);
      this.resultData1.splice(index, 1);

      console.log(status);
    }
  }
};
</script>
<style></style>
