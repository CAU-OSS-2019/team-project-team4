<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Success Missions</h3>
        </div>
        <div class="col text-right"></div>
      </div>
    </div>

    <div class="table-responsive mt-3">
      <base-table type="hover" thead-classes="thead-light" :data="propsdata">
        <template slot="columns">
          <th>후원인</th>
          <th>후원내역</th>
        </template>

        <template class="align-items-center" slot-scope="row">
          <th scope="row" width="10px">{{ propsdata[row.index][1] }}</th>
          <td class="align-content-center">{{ propsdata[row.index][2] }}</td>
        </template>
      </base-table>
    </div>
  </div>
</template>

<script>
export default {
  props: ["propsdata"],
  name: "success-mission"
};
</script>
<style>
</style>
