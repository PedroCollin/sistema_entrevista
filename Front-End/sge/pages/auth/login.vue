<template>
  <div class="master">
    <div class="container">
      <div class="forms">
        <div class="form login">
          <div class="title-container">
            <span class="title">Login</span>
            <div class="imgbosch"></div>
          </div>
          <form @submit.prevent="enviarLogin">
            <div class="input-field">
              <input
                type="text"
                placeholder="Entre com seu e-mail"
                v-model="email"
                required
              />
              <i class="uil uil-envelope icon"></i>
            </div>
            <div class="input-field">
              <input
                type="password"
                class="password"
                placeholder="Entre com sua senha"
                v-model="senha"
                required
              />
              <i class="uil uil-lock icon"></i>
              <i class="uil uil-eye-slash showHidePw"></i>
            </div>



            <div class="input-field button">
              <input type="submit" value="Login" />
            </div>
          </form>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { mapState } from "vuex";

export default {
  data() {
    return {
      email: "",
      senha: "",
    };
  },
  methods: {
    async enviarLogin() {
      const responseToken = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          email: this.email,
          password: this.senha,
        }),
      });
      const token = await responseToken.json();
      console.log(token.jwt);
      try {
        const response = await fetch("http://127.0.0.1:8000/api/user/", {
          headers: { "Content-Type": "application/json" },
          credentials: "include",
        });
        const content = await response.json();
        console.log(content);
        if (content.detail == "Deslogado!") {
          console.log("deu errado");
        } else {
          this.$store.commit("STORE_SESSION", content);
          this.$store.commit("STORE_TOKEN", token.jwt);
          console.log("deu certo");
        }
      } catch (e) {}
      // this.syncDelay(5000)
      // this.$router.go("/");
      this.$router.push({ path: "/" });
    },
  },
  computed: {
    ...mapState({
      user_session: (state) => state.user_session,
      token: (state) => state.token,
    }),
  },
};
</script>

<style scoped src="@/static/auth/login.css">
</style>
