<template>
  <div class="container">
    <div class="all">
      <br>
      <div class="all" v-if="auth">
        <a href="../../auth/login" class="py-5 px-3" @click="logout">Logout</a>
      </div>
      <br>
      <h2>Bem vindo {{user.nome}}!</h2>
    </div>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
  </div>
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
      await fetch("http://127.0.0.1:8000/api/logout/", {
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
