<template>
  <div class="cen">
    <div v-if="auth">
        <h1>Você esta Logado!</h1>
    </div>
    <form class="form" @submit.prevent="enviarRegister">
      <div class="mb-4">
        <label for="nome"> Nome </label>
        <input
          id="nome"
          type="text"
          placeholder="Nome completo"
          v-model="nome"
        />
      </div>
      <div class="mb-4">
        <label for="edv"> Edv </label>
        <input id="edv" type="text" placeholder="EDV" v-model="edv" />
      </div>
      <div class="mb-4">
        <label for="email"> Email </label>
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
        <button type="submit">Cadastrar</button>

        <p class="edit-p">
          <nuxt-link to="/">home</nuxt-link>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data: () => ({
    nome: "",
    edv: "",
    email: "",
    senha: "",
    auth: false,
  }),
  async mounted() {
    this.$nuxt.$on("auth", (auth) => {
      this.auth = auth;
    });
  },
  created() {
    if (this.$store.state.user_session.id != null) {
      this.auth = true;
    } 
    // else {
    //   this.$router.push("/auth/login/");
    // }
  },
  methods: {
    async enviarRegister() {
      console.log(this.$store.state.token);
      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: this.$store.state.token,
        },
        body: JSON.stringify({
          nome: this.nome,
          email: this.email,
          edv: this.edv,
          password: this.senha,
        }),
      });
      console.log(response);
      await this.$router.push("/auth/login/");
    },
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
