template>
  <div class="col-md-2">
    <base-button block type="success" class="mb-3" @click="WhoIsMissionKing()">MissionKing</base-button>

    <modal
      :show.sync="modals.modal2"
      gradient="success"
      modal-classes="modal-success modal-dialog-centered"
    >
      <h6 slot="header" class="modal-title" id="modal-title-notification">누가 미션을 가장 많이 걸었을까요?</h6>

      <div class="py-3 text-center">
        <ul>
          <li v-for="man in missionkingData">{{ man[0] }} 님께서 {{ man[1] }} 번의 미션을 거셨습니다.</li>
        </ul>
      </div>

      <template slot="footer">
        <base-button
          type="link"
          text-color="white"
          class="ml-auto"
          @click="modals.modal2 = false"
        >Close</base-button>
      </template>
    </modal>
  </div>
</template>


<script>
import Modal from "../../components/Modal.vue";

export default {
  props: ["propsdata"],
  components: {
    Modal
  },

  data() {
    return {
      missionkingData: [],
      modals: {
        modal2: false
      },
      missionking: null
    };
  },

  methods: {
    WhoIsMissionKing: function() {
      this.missionking = new Map();
      for (var i = 0; i < this.propsdata.length; i++) {
        if (this.missionking.has(this.propsdata[i][1])) {
          let temp = this.missionking.get(this.propsdata[i][1]);
          this.missionking.set(this.propsdata[i][1], temp + 1);
        } else {
          this.missionking.set(this.propsdata[i][1], 1);
        }
      }
      this.missionkingData = [...this.missionking.entries()].sort(
        (a, b) => b[1] - a[1]
      );
      if (this.missionkingData.length >= 6)
        this.missionkingData.splice(5, this.missionkingData.length - 5);
      this.modals.modal2 = true;
    }
  }
};
</script>
<style></style>
