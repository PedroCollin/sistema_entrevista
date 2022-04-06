<template>
  <div class="container">
    <div class="form">
      <form @submit.prevent="enviarLogin">
        <div class="input-field">
          <input
            type="text"
            placeholder="Nome da dinâmica"
            v-model="nome_dinamica"
            required
          />
        </div>
        <div class="input-field">
          <input type="time" class="time" v-model="duracao_dinamica" required />
        </div>
        <Divider />

        <span class="desc">
          <Textarea
            id="textarea"
            v-model="value10"
            rows="5"
            cols="120"
            placeholder="Descreva a dinâmica aqui"
          ></Textarea>
        </span>
        <Panel header="Criterios da dinâmica">
          <div class="addCriterio">
            <div class="input-field">
              <input
                type="text"
                placeholder="Nome da dinâmica"
                v-model="nome_dinamica"
                required
              />
            </div>
            <Divider layout="vertical" />

            <div class="input-field">
              <input
                type="number"
                placeholder="Peso da dinâmica"
                v-model="peso_dinamica"
                required
              />
            </div>
            <Button label="Success" class="p-button-raised p-button-success p-button-text"></Button>
          </div>
        </Panel>
      </form>
    </div>
  </div>
</template>

<script>
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Divider from 'primevue/divider'
import Panel from 'primevue/panel'
import Button from 'primevue/button';
export default {
  components: {
    InputText: InputText,
    Textarea: Textarea,
    Divider: Divider,
    Panel: Panel,
    Button: Button,
  },
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  background-origin: border-box;
}

.container {
  display: flex;
  height: 90vh;
  justify-content: center;
  align-items: center;
  padding: 20vh;
  background-color: #e6e6e6;
}

.form {
  max-width: 50vw;
  min-width: 300px;
  width: 100%;
  background-color: #fff;
  padding: 20px 20px;
  border-radius: 5px;
  font-size: 19px;
}

.form .input-field {
  position: relative;
  height: 50px;
  width: 100%;
  margin-top: 30px;
}

.form Textarea {
  max-width: 100%;
  max-height: 150px;
}

.desc {
  margin-top: 30px;
}

.addCriterio {
  display: flex;
  flex-direction: row;
}

.input-field input {
  position: absolute;
  height: 100%;
  width: 100%;
  padding: 0 10px;
  border: none;
  outline: none;
  font-size: 16px;
  border-bottom: 2px solid #ccc;
  border-top: 2px solid transparent;
  transition: all 0.2s ease;
}

.time {
  width: 150px !important;
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
.form .button input {
  border: none;
  color: #fff;
  font-size: 17px;
  font-weight: 500;
  letter-spacing: 1px;
  border-radius: 6px;
  background-color: #4070f4;
  cursor: pointer;
  transition: all 0.3s ease;
}
.button input:hover {
  background-color: #265df2;
}
</style>