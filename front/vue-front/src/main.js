import Vue from "vue";
import App from "./App.vue";
import axios from "axios";
import VueAxios from "vue-axios";
import router from "./router";
import "./registerServiceWorker";
import ArgonDashboard from "./plugins/argon-dashboard";

Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

Vue.use(ArgonDashboard);
new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
