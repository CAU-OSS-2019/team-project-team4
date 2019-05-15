<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div>
        <div class="text-center">
          <router-link class="base-nav col-lg-10" to="/">
            <base-button type="twitch col-lg-5" icon="fa fa-twitch" >Login</base-button>
          </router-link>
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
