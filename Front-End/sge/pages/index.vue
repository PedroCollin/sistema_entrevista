<template>
  <Carousel :value="cars" :numVisible="4" :numScroll="3" :responsiveOptions="responsiveOptions">
    <template #header>
      <h2>Basic</h2>
    </template>
    <template #item="slotProps">
      <div class="car-item">
              <div class="car-content">
                  <div>
                      <img :src="'demo/images/car/' + slotProps.data.brand + '.png'" :alt="slotProps.data.brand" />
                  </div>
                  <div>
                      <div class="car-title">{{slotProps.data.brand}}</div>
                      <div class="car-subtitle">{{slotProps.data.year}} | {{slotProps.data.color}}</div>

                      <div class="car-buttons">
                          <Button icon="pi pi-search" class="p-button-secondary" />
                          <Button icon="pi pi-star-fill" class="p-button-secondary" />
                          <Button icon="pi pi-cog" class="p-button-secondary" />
                      </div>
                  </div>
              </div>
          </div>
    </template>
  </Carousel>
</template>

<script>
import { mapState } from "vuex";

export default {
  layout: 'default',
  data() {
    return {
      auth: false,
      user:""
    };
  },
  async mounted() {
   
    this.$nuxt.$on("auth", (auth) => {
      this.auth = auth;
    });
    
    this.user = this.$store.state.user_session
  },
  created(){
    if(this.$store.state.user_session.id != null) {
      this.auth = true
    }
    else{
      this.$router.push('/auth/login/');
    }
  },
  computed: {
    ...mapState({
        user_session: (state) => state.user_session,
        token: (state) => state.token,
    }),
  },
  methods: {
    async logout() {
      await fetch("http://127.0.0.1:8000/api/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      this.auth = false;
      this.$store.commit("STORE_SESSION", {});
      this.$store.commit("STORE_TOKEN", {});
      await this.$router.push("/auth/login/");
    },
  },
};
</script>

<style scoped>

.container{
  background-color: rgb(248, 248, 248);
  align-content: center;
  justify-content: center;
}

.all{ 
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-left: 45%;
}

</style>
