<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Missions</h3>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table thead-classes="thead-light" :data="propsdata">
        <template slot="columns">
          <th>후원인</th>
          <th>후원내역</th>
        </template>

        <template slot-scope="row">
          <th scope="row">{{ propsdata[row.index][1] }}</th>
          <td>{{ propsdata[row.index][2] }}</td>
        </template>
      </base-table>
    </div>
  </div>
</template>
<script>
export default {
  props: ["propsdata"],
  name: "page-visits-table"
};
</script>
<style>
</style>
