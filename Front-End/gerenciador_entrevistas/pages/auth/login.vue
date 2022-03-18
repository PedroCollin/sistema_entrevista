<template>
  <div class="cen">
    <form class="form" @submit.prevent="enviarLogin">
      <div class="mb-4">
        <label for="edv"> Email </label>
        <input id="email" type="text" placeholder="Email" v-model="email" />
      </div>
      <div class="mb-6">
        <label for="password"> Senha </label>
        <input
          id="password"
          type="password"
          placeholder="******************"
          v-model="senha"
        />
        <button type="submit">Login</button>

        <p class="edit-p">
          não tem uma conta?
          <a href="../../auth/register">Cadastrar</a>
          <nuxt-link to="/">home</nuxt-link>
        </p>
      </div>
    </form>
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
      console.log(token.jwt)
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

<style>
.cen {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}
</style>
