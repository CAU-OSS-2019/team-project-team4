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


        <template class="align-items-center" slot-scope="row" v-if="fitDate[row.index]">
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
                    <div class="text-center text-muted mb-4">
                        <small class="fa fa-edit">Modify mission</small>
                    </div>
                    <form role="form">
                      <input  type="text"
                        class="form-control mb-2"
                        placeholder="Mission"
                        v-model="missions">
                        <div class="text-center">
                            <base-button type="primary" class="text-right my-4">close</base-button>
                            <base-button type="primary" class="test-right my-4">Modify</base-button>
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
        <div class="col text-right pb-3">
          <base-button outline
                type="twitch"
                size="sm"
                icon="fa fa-edit"
                v-on:click="fit()">
          date Select
          </base-button>
          <base-button outline
                type="twitch"
                size="sm"
                icon="fa fa-edit"
                v-on:click="modals.modal1 = true">
          Create
          </base-button>
          <modal :show.sync="modals.modal1">
            <template slot="header">
                <h5 class="modal-title" id="exampleModalLabel">Create Mission</h5>
            </template>
            <div>
              <form role="form">
                    <input  type="text"
                        class="form-control mb-2"
                        placeholder="Donator"
                        v-model="donators">
                    <input type="text"
                            class="form-control"
                            placeholder="Mission"
                            v-model="missions">
              </form>
            </div>
            <template slot="footer">
                <base-button type="secondary" @click="modals.modal1 = false">Cancel</base-button>
                <base-button type="primary">Save Mission</base-button>
            </template>
          </modal>
            
        </div>
      </div>
          <div class="input-daterange datepicker row align-items-center">
          <div class="col">
              <div class="form-group">
                  <div class="input-group input-group-alternative">
                      <div class="input-group-prepend">
                          <span class="input-group-text"><i class="ni ni-calendar-grid-58"></i></span>
                      </div>
                      <input class="form-control" placeholder="Start date" type="text" v-model="start_date">
                  </div>
              </div>
          </div>
          <div class="col">
              <div class="form-group">
                  <div class="input-group input-group-alternative">
                      <div class="input-group-prepend">
                          <span class="input-group-text"><i class="ni ni-calendar-grid-58"></i></span>
                      </div>
                      <input class="form-control" placeholder="End date" type="text" v-model="end_date">
                  </div>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>
<script>
import Modal from "@/components/Modal.vue";
export default {
  props: ["propsdata"],
  name: "mission-table",
  components: {
    Modal
  },
  data() {
    return {
      modals: {
        modal0: false,
        modal1: false
      },
      start_date : "2019-01-01",
      end_date : "2019-10-10",
      fitDate : []
    };
  },
  methods: {
    manage: function(index, status) {
      this.$emit("manage", index, status);
      // Imediately refresh
      this.axios.post("/get_result")
      .then(function(response) {
        this.resultDataTemp = response.data;
        this.trimResultData();
      })
      .catch(function() {
        console.log("refresh error");
      });
    },
    setDate: function() {
      this.start_date = this.propsdata[0][4];
      this.end_date = this.propsdata[0][4];
    },
    fit: function() {
      var start = new Date(this.start_date);
      var end = new Date(this.end_date);
      for (var i = 0; i < this.propsdata.length; i++) {
        var compare = new Date(this.propsdata[i][4]);
        if (start <= compare && end >= compare){
          this.fitDate[i]=true;
        }
        else{
          this.fitDate[i]=false;
        }
      }
      console.log(this.fitDate);
    },
  },
  mounted() {
    this.setDate();
    this.fit()
    this.setRefresh();
    console.log("mounted");
  },
};



</script>
<style>
</style>
