<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Missions</h3>
        </div>
        <div class="col text-right">
            <base-button type="twitch" outline size="sm" @:click="refresh()">Refresh</base-button>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table type="hover" thead-classes="thead-light" :data="propsdata">
        <template slot="columns">
          <th>후원인</th>
          <th>후원내역</th> 
          <th>Success</th>
          <th>fail</th>
          <th>Modify</th>
          <th class="text-right">Etc</th> 
        </template>


        <template class="align-items-center" slot-scope="row">
          <th scope="row" width="10px">
            {{ propsdata[row.index][1] }}
          </th>
          <td class="align-content-center">
              {{ propsdata[row.index][2] }}
          </td>
          <td class="text-right" width="1px">
            <base-button
                outline iconOnly
                type="twitch"
                size="sm"
                icon="fa fa-check-square"
                v-on:click="manage(row.index, 'mission_success')"
            >
            </base-button>
            </td>
            <td class="text-right" width="1px">
              <base-button 
                outline iconOnly
                type="twitch"
                icon="fa fa-check-square"
                v-on:click="manage(row.index, 'mission_fail')"
                size="sm"
                ></base-button>
            </td>
            <td class="text-right" width="1px">
              <base-button
                outline iconOnly
                type="twitch"
                size="sm"
                icon="fa fa-edit"
                v-on:click="modals.modal0 = true"
            ></base-button>
              <modal :show.sync="modals.modal0"
                      body-classes="p-0"
                      modal-classes="modal-dialog-centered modal-sm">
                      <card type="secondary" shadow
                  header-classes="bg-white pb-5"
                  body-classes="px-lg-5 py-lg-5"
                  class="border-0">
                <template>
                    <div class="text-muted text-center mb-3">
                        <small>Sign in with</small>
                    </div>
                    <div class="btn-wrapper text-center">
                        <base-button type="neutral">
                            <img slot="icon" src="https://demos.creative-tim.com/argon-design-system/assets/img/icons/common/github.svg">
                            Github
                        </base-button>

                        <base-button type="neutral">
                            <img slot="icon" src="https://demos.creative-tim.com/argon-design-system/assets/img/icons/common/google.svg">
                            Google
                        </base-button>
                    </div>
                </template>
                <template>
                    <div class="text-center text-muted mb-4">
                        <small>Or sign in with credentials</small>
                    </div>
                    <form role="form">
                        <base-input alternative
                                    class="mb-3"
                                    placeholder="Email"
                                    addon-left-icon="ni ni-email-83">
                        </base-input>
                        <base-input alternative
                                    type="password"
                                    placeholder="Password"
                                    addon-left-icon="ni ni-lock-circle-open">
                        </base-input>
                        <base-checkbox>
                            Remember me
                        </base-checkbox>
                        <div class="text-center">
                            <base-button type="primary" class="my-4">Sign In</base-button>
                        </div>
                    </form>
                </template>
            </card>   
              </modal>
            </td>
              <td class="text-right" width="1px">
              <base-dropdown 
                class="media" 
                icon="fas fa-ellipsis-v"
                position="right">
                  <div class="media align-items-center" slot="title">
                    <div class="media-body ml-2 d-none d-lg-block">
                        <i class="fas fa-ellipsis-v"></i>
                    </div>
                  </div>
                  <template>
                    <base-button block class="dropdown-item" outline size="sm" @click="manage(row.index, 'mission_delete')">
                          <i class = "fa fa-trash text-twitch"></i>
                          <span class = "text-twitch">Delete</span>
                    </base-button>
                  </template>
              </base-dropdown>
            </td>
        </template>
      </base-table>
    </div>
    <div class="card-footer border-0">
      <div class="row align-items-center">
        <div class="col text-right">
          <base-button outline
                type="twitch"
                size="sm"
                icon="fa fa-edit"
                v-on:click="modals.modal1 = true">
          Create
          </base-button>
          <modal :show.sync="modals.modal1">
            <template slot="header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            </template>
            <div>
              ...
            </div>
            <template slot="footer">
                <base-button type="secondary" @click="modals.modal1 = false">Close</base-button>
                <base-button type="primary">Save changes</base-button>
            </template>
          </modal>
            
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Modal from "@/components/Modal.vue";
export default {
  props: ["propsdata"],
  name: "page-visits-table",
  components: {
    Modal
  },
  data() {
    return {
      modals: {
        modal0: false,
        modal1: false
      }
    };
  },
  methods: {
    manage: function(index, status) {
      this.$emit("manage", index, status);
    }
  }
};
</script>
<style>
</style>
