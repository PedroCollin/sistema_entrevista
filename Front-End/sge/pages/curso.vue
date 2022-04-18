<template>
  <div class="painel">
    <div class="painel-image"></div>
    <div class="painel-form">
      <div class="form">
        <form @submit.prevent="enviarLogin">
          <div class="input-field">
            <input type="text" placeholder="Nome da dinâmica" required />
          </div>
          <div class="flex-row">
            <div class="input-field">
              <input
                type="text"
                step="2"
                class="periodo"
                placeholder="Perido do Curso"
                required
              />
            </div>
            <Divider class="dividerCri" layout="vertical" />
            <div class="input-field">
              <input
                type="number"
                step="2"
                class="hora"
                placeholder="Carga horaria"
                required
              />
            </div>
          </div>

          <Divider />
          <span class="desc">
            <Textarea
              id="textarea"
              rows="5"
              cols="90"
              placeholder="Descreva a dinâmica aqui"
              class="descricao"
            ></Textarea>
          </span>
          <div class="button-bottom">
            <Button
              label="Registrar Curso"
              class="p-button-raised p-button-success"
              @click="enviarDinamica"
            ></Button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.painel {
  width: 100%;
  height: 93vh;
  background-color: #f7f7f7;
  display: flex;
  flex-direction: row;
}

.painel-image {
  background-color: aquamarine;
  width: 50%;
  height: 100%;
  background-image: url('./../assets/images/editado.jpg');
  background-repeat: no-repeat;
  background-size: cover;
}

.painel-form {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 2.5rem;
  padding-top: 1rem;
}

.flex-row {
  width: 100%;
  display: flex;
  flex-direction: row;
}

.input-field .periodo {
  width: 100%;
  margin-right: 1rem;
}

.input-field .hora {
  width: 100%;
}

.dividerCri {
  margin-top: 35px;
  margin-bottom: 10px;
  height: 40px;
}

.descricao {
  max-width: 100%;
  max-height: 50vh;
  width: 100%;
  height: 50vh;
}

.button-bottom{
  display: flex;
  flex-direction: row;
  justify-content: right;
  margin-top: 30px;
}
/* --------------------------------------------------------------------------------- */

.form .input-field {
  position: relative;
  height: 35px;
  width: 100%;
  margin-top: 30px;
}

.input-field input {
  position: absolute;
  height: 7vh;
  min-height: 7vh;
  width: 100%;
  padding: 0 10px;
  border: none;
  outline: none;
  font-size: 19px;
  border-bottom: 2px solid #ccc;
  border-top: 2px solid transparent;
  transition: all 0.2s ease;
  border-radius: 0.2rem;
}

.input-field input:is(:focus, :valid) {
  border-bottom-color: #4070f4;
}
.input-field input:is(:focus, :valid) ~ i {
  color: #4070f4;
}
.input-field textarea:is(:focus, :valid) {
  border-bottom-color: #4070f4;
}
.input-field textarea:is(:focus, :valid) ~ i {
  color: #4070f4;
}
.checkbox-content input {
  margin: 0 8px -2px 4px;
  accent-color: #4070f4;
}
.form .text {
  color: #333;
  font-size: 14px;
}
.form a.text {
  color: #4070f4;
  text-decoration: none;
}
.form a:hover {
  text-decoration: underline;
}
.form .button {
  margin-top: 400px;
}

@media screen and (max-width: 720px) {
  .painel {
    flex-direction: column;
  }

  .painel-image {
    width: 100%;
    height: 50%;
  }

  .painel-form {
    width: 100%;
    height: 50%;
  }
}
</style>
