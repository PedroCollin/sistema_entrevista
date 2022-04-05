<template>
  <div>
    <Header />
    <div class="master">
      <div class="container">
        <div class="forms">
          <div class="form dinamica">
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
                <input
                  type="time"
                  class="time"
                  v-model="duracao_dinamica"
                  required
                />
              </div>
              <div class="input-field">
                <textarea
                  placeholder="Descreva a dinâmica aqui"
                  class="descricao"
                  v-model="descricao_dinamica"
                  required
                />
              </div>

              <div class="area-criterio">
                <form @submit.prevent="enviarLogin" class="form-criterio">
                  <div class="input-field">
                    <input
                      type="text"
                      placeholder="Nome do criterio"
                      v-model="nome_dinamica"
                      required
                    />
                  </div>
                  <div class="separator">|</div>
                  <div class="input-field">
                    <input
                      type="number"
                      placeholder="Peso do criterio"
                      v-model="nome_dinamica"
                      required
                    />
                  </div>
                  <input
                    class="button_adicionar"
                    type="button"
                    value="Adicionar"
                  />
                </form>
                <table>
                    <tr id="header">
                        <th>Critério</th>
                        <th>Peso</th>
                    </tr>
                    <tr>
                        <td>Trabalho em equipe</td>
                        <td>2</td>
                    </tr>
                </table>
              </div>

              <div class="input-field button">
                <input type="submit" value="Login" />
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
/* ===== Google Font Import - Poformsins ===== */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

.master {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ebebeb;
}

.container {
  position: relative;
  max-width: 950px;
  width: 100%;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin: 20px 20px;
}

.container .forms {
  display: flex;
  align-items: center;
  height: 100%;
  width: 200%;
  transition: height 0.2s ease;
}

.container .form {
  width: 50%;
  height: 800px;
  padding: 30px;
  padding-top: 1px;
  background-color: #fff;
  transition: margin-left 0.18s ease;
}

.container.active .dinamica {
  margin-left: -50%;
  opacity: 0;
  transition: margin-left 0.18s ease, opacity 0.15s ease;
}

.container .signup {
  opacity: 0;
  transition: opacity 0.09s ease;
}
.container.active .signup {
  opacity: 1;
  transition: opacity 0.2s ease;
}

.container.active .forms {
  height: 600px;
}

.form .input-field {
  position: relative;
  height: 50px;
  width: 100%;
  margin-top: 30px;
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

.area-criterio {
  position: absolute;
  border: 1px solid #ccc;
  margin-top: 160px;
}

.input-field textarea {
  position: absolute;
  height: 200px;
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

textarea {
  width: 100%;
  height: 150px;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  font-size: 16px;
  resize: none;
}

.area-criterio {
  width: 90%;
  position: absolute;
}

.form-criterio {
  display: flex;
  flex-direction: row;
  transition: margin-left 0.18s ease;
}

.form-criterio .button_adicionar {
  border: none;
  color: #fff;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.2px;
  border-radius: 4px;
  background-color: #4070f4;
  cursor: pointer;
  transition: all 0.3s ease;
  margin: 30px 10px 5px 10px;
  padding: 5px;
}

.separator{
    display: flex;
    justify-content: end;
    align-items: flex-end;
    font-size: 22px;
    margin-bottom: 6px;
}

table{
    position: absolute;


    border-collapse:collapse;
    width: 100%;
    
}
</style>