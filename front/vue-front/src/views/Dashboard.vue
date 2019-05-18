<template>
  <div>
    <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8"></base-header>

    <div class="container-fluid mt--7">
      <div class="row mt-5">
        <div class="col-xl-8 mb-5 mb-xl-0">
          <page-visits-table v-bind:propsdata="resultData"></page-visits-table>
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

export default {
  components: {
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
        ]
      ]
    };
  },

  methods: {
    initBigChart(index) {
      let chartData = {
        datasets: [
          {
            label: "Performance",
            data: this.bigLineChart.allData[index]
          }
        ],
        labels: ["May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
      };
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    }
  },
  mounted() {
    this.initBigChart(0);
  }
};
</script>
<style></style>
