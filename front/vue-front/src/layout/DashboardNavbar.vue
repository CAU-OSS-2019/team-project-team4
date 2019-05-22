<template>
  <base-nav class="navbar-top navbar-dark" id="navbar-main" :show-toggle-button="false" expand>
    <form class="navbar-search navbar-search-dark form-inline mr-3 d-none d-md-flex ml-lg-auto"/>
    <ul class="navbar-nav align-items-center d-none d-md-flex">
      <li class="nav-item dropdown">
        <base-dropdown position="right" class="nav-link pr-5">
          <div class="media align-items-center" slot="title">
            <span class="avatar avatar-sm rounded-circle" v-if="profile_image_url.length!=0">
              <img v-bind:src="profile_image_url" />
            </span>
            <div class="media-body ml-2 d-none d-lg-block">
              <span class="mb-0 text-sm font-weight-bold" v-if="userName.length!=0">{{userName}}</span>
            </div>
          </div>
          <template>
            <div class="dropdown-header noti-title">
              <h6 class="text-overflow m-0">Welcome {{userName}}!!</h6>
            </div>
            <div class="dropdown-item">
              <i class="fa fa-sign-out"></i>
              <span v-on:click="logout()">Logout</span>
            </div>
          </template>
        </base-dropdown>
      </li>
    </ul>
  </base-nav>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchQuery: "",
      userName: "",
      profile_image_url: ""
    };
  },
  created() {
    axios.post('/get_userinfo')
    .then((res) => {
      this.userName = res.data[0]
      this.profile_image_url = res.data[1]
      console.log(this.userName, this.profile_image_url)
    })
  },
  methods: {
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    logout() {
      axios.post('/logout')
      .then((res) => {
        window.location.pathname = '/'
      })
    }
  },
};
</script>
