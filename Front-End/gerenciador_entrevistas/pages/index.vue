<template>
  <div>
    <div>
      <h1>Bem vindo!</h1>
      <h3>Seus dados</h3>
      <h5>{{user.id}}</h5>
      <h5>{{user.nome}}</h5>
      <h5>{{user.edv}}</h5>
      <h5>{{user.email}}</h5>
    </div>
    <div v-if="auth">
      <a href="#" class="py-5 px-3" @click="logout">Logout</a>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
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
