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
            <base-button
              outline
              type="default"
              v-on:click="manage(row.index, 'mission_success')"
            >Success</base-button>
          </th>
          <td>
            <base-button outline type="default" v-on:click="manage(row.index, 'mission_fail')">Fail</base-button>
          </td>
          <td>
            <base-button
              outline
              type="default"
              v-on:click="manage(row.index, 'mission_delete')"
            >Delete</base-button>
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
    manage: function(index, status) {
      this.$emit("manage", index, status);
    }
  }
};
</script>
<style>
</style>
