<template>
  <div class="master">
    <div class="wrapper">
      <h2>Cadastro</h2>
      <form @submit.prevent="enviarRegister">
        <div class="input-box">
          <input
            type="text"
            placeholder="Entre com seu nome completo"
            v-model="nome"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="number"
            placeholder="Entre com seu EDV"
            v-model="edv"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="email"
            placeholder="Enter com seu e-mail"
            v-model="email"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="password"
            placeholder="Entre com sua senha"
            v-model="senha"
            required
          />
        </div>
        <div class="input-box button">
          <input type="Submit" value="Cadastrar" />
        </div>
        <div class="text">
          <h3>
            Já tem uma conta? <a href="../auth/login">Efetuar login</a>
          </h3>
        </div>
      </form>
    </div>
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

<style scoped src="@/static/auth/register.css">
</style>