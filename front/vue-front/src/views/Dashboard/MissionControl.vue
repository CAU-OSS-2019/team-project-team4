<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Mission Control</h3>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table thead-classes="thead-light" :data="propsdata">
        <template slot="columns">
          <th></th>
        </template>

        <template slot-scope="row">
          <th scope="row">
            <base-button outline type="default" v-on:click="success(row.index)">Success</base-button>
          </th>
          <td>
            <base-button outline type="default">Fail</base-button>
          </td>
          <td>
            <base-button outline type="default">Delete</base-button>
          </td>
        </template>
      </base-table>
    </div>
  </div>
</template>
<script>
export default {
  props: ["propsdata"],
  name: "mission-control",
  methods: {
    success: function(index) {
      this.$emit("success", index);
      console.log(this.propsdata);
    }
  }
};
</script>
<style>
</style>
