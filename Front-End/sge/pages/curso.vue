<template>
  <div class="painel">
    <div class="painel-image"></div>
    <div class="painel-form">
      <form action="">
        <div class="input-field">
          <input type="text" placeholder="Nome do Curso" required />
        </div>
      </form>
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
  background-color: #F7F7F7;
  display: flex;
  flex-direction: row;
}

.painel-image {
  background-color: aquamarine;
  width: 50%;
  height: 100%;
  background-image: url("./../assets/images/editado.jpg") ;
  background-repeat: no-repeat;
  background-size: cover;
}

.painel-form {

  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 3rem;
}

/* --------------------------------------------------------------------------------- */

.form .input-field {
  position: relative;
  height: 50px;
  width: 100%;
  margin-top: 30px;
}

.input-field input {
  position: absolute;
  height: 5vh;
  width: 45vw;
  padding: 0 10px;
  border: none;
  outline: none;
  font-size: 16px;
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
