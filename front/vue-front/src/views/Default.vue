<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div>
        <div class="text-center">
          <base-button type="twitch col-lg-5" v-on:click="gotoLogin">Login</base-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "default",
  methods: {
    gotoLogin() {
      window.location.pathname = "/login";
    }
  }
};
</script>
<style>
</style>
