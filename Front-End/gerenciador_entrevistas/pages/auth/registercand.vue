<template>
  <div class="master">
    <div class="wrapper">
      <h2>Cadastro</h2>
      <form @submit.prevent="enviarRegister">
        <div class="input-box">
          <input
            type="text"
            placeholder="Entre com o nome completo"
            v-model="nome"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="number"
            placeholder="Entre com o CPF"
            v-model="cpf"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="email"
            placeholder="Entre com a Data de Nascimento"
            v-model="datanasc"
            required
          />
        </div>
        <div class="input-box">
          <input
            type="password"
            placeholder="Entre com a turma"
            v-model="turma"
            required
          />
        </div>
        
        <br>
        <input type="file"
       id="avatar" name="avatar"
       accept="image/png, image/jpeg">
       <br>

        <div class="input-box button">
          <input type="Submit" value="Cadastrar" />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    nome: "",
    cpf: "",
    datanasc: "",
    turma: "",
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
          datanasc: this.datanasc,
          cpf: this.cpf,
          turma: this.turma,
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