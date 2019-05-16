<template>
  <base-nav class="navbar-top navbar-dark" id="navbar-main" :show-toggle-button="false" expand>
    <form class="navbar-search navbar-search-dark form-inline mr-3 d-none d-md-flex ml-lg-auto"/>
    <ul class="navbar-nav align-items-center d-none d-md-flex">
      <li class="nav-item dropdown">
        <base-dropdown class="nav-link pr-5">
          <div class="media align-items-center" slot="title">
            <span class="avatar avatar-sm rounded-circle">
              <i class="twitch fa fa-user-circle"></i>
            </span>
            <div class="media-body ml-2 d-none d-lg-block">
              <span class="mb-0 text-sm font-weight-bold">(userName){{userName}}</span>
            </div>
          </div>
          <template>
            <div class="dropdown-header noti-title">
              <h6 class="text-overflow m-0">Welcome {{userName}}!!</h6>
            </div>
            <router-link to="/" class="dropdown-item">
              <i class="fa fa-sign-out"></i>
              <span>Logout</span>
            </router-link>
          </template>
        </base-dropdown>
      </li>
    </ul>
  </base-nav>
</template>
<script>
export default {
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchQuery: "",
      userName: "",
    };
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
    }
  }
};
</script>
