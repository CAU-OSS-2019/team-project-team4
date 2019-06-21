<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Fail Missions</h3>
        </div>
        <div class="col text-right"></div>
      </div>
    </div>

    <div class="table-responsive mt-3">
      <base-table type="hover" thead-classes="thead-light" :data="failmission">
        <template slot="columns">
          <th>후원인</th>
          <th>후원내역</th>
        </template>

        <template class="align-items-center" slot-scope="row">
          <div class="col mb-5">
            <th scope="row" width="10px">{{ failmission[row.index][1] }}</th>
            <td class="align-content-center">{{ failmission[row.index][2] }}</td>
          </div>
        </template>
      </base-table>
    </div>
  </div>
</template>

<script>
export default {
  props: ["failmission"],
  name: "fail-mission"
};
</script>
<style>
</style>
