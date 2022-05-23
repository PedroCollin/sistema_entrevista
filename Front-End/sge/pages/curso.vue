<template>
  <div class="painel">
    <toast position="top-right" />
    <div class="painel-image"></div>
    <div class="painel-form">
      <div class="form">
        <form>
          <div class="input-field">
            <input
              type="text"
              placeholder="Nome do curso"
              v-model="curso.titulo"
              required
            />
          </div>
          <div class="flex-row">
            <div class="input-field">
              <Dropdown
                class="dropdown"
                v-model="curso.periodo"
                :options="periodos"
                optionLabel="name"
                placeholder="Selecione um periodo"
              />
            </div>
            <Divider class="dividerCri" layout="vertical" />
            <div class="input-field">
              <input
                type="number"
                step="2"
                class="hora"
                placeholder="Carga Horária"
                v-model="curso.carga_horaria"
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
              placeholder="Descrição do Curso"
              class="descricao"
              v-model="curso.descricao"
            ></Textarea>
          </span>
          <div class="button-bottom">
            <Button
              label="Registrar Curso"
              class="p-button-raised p-button-success"
              @click="enviarCurso"
            ></Button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedPeriodo: null,
      periodos: [
        { name: 'Manhã', code: 'Manha' },
        { name: 'Tarde', code: 'Tarde' },
        { name: 'Noite', code: 'Noite' },
      ],
      curso: {
        titulo: "",
        descricao: "",
        periodo: "",
        carga_horaria: "",
      },
    }
  },
  methods: {
    async enviarCurso() {
      console.log(this.curso)
      if (
        this.curso.titulo == "" ||
        this.curso.descricao == "" ||
        this.curso.periodo == "" ||
        this.curso.carga_horaria == ""
      ) {
        this.$toast.add({
          severity: 'error',
          summary: 'Preencha todos os campos!',
          detail: 'Error ',
          life: 3000,
        })
      } else {
        try {
          const responseToken = await fetch(
            'http://127.0.0.1:8000/api/main/curso/',
            {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              credentials: 'include',
              body: JSON.stringify([
                {
                  titulo: this.curso.titulo,
                  descricao: this.curso.descricao,
                  periodo: this.curso.periodo.name,
                  carga_horaria: this.curso.carga_horaria,
                },
              ]),
            }
          )
          if (responseToken.status != '200') {
            this.$toast.add({
              severity: 'error',
              summary: 'Erro ao registrar nova dinâmica',
              detail: 'Error: ' + responseToken.status,
              life: 3000,
            })

            this.curso.titulo = ""
            this.curso.descricao = ""
            this.curso.periodo.name = ""
            this.curso.carga_horaria = ""
          } else {
            this.$toast.add({
              severity: 'success',
              summary: 'Dinâmica cadastrada com sucesso',
              detail: 'Dinâmica registrada',
              life: 3000,
            })
          }
          console.log(responseToken)
        } catch (error) {
          this.$toast.add({
            severity: 'error',
            summary: 'Preencha todos os campos!',
            detail: 'Error: ' + error,
            life: 3000,
          })
        }
      }
    },
  },
}
</script>

<style scoped>
.painel {
  width: 100%;
  height: 92vh;
  background-color: #f7f7f7;
  display: flex;
  flex-direction: row;
}

.painel-image {
  width: 50%;
  height: 100%;
  background-image: url('./../assets/images/editado.jpg');

  background-repeat: no-repeat center center;
  background-size: cover;
}

.painel-form {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 3.5rem;
  padding-top: 1rem;
  margin-bottom: 55px;
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

.p-dropdown {
}

.button-bottom {
  display: flex;
  flex-direction: row;
  justify-content: right;
  align-content: top;
  margin-top: 5%;
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
  height: 3.2rem;
  min-height: 3rem;
  width: 100%;
  padding: 0 10px;
  border: none;
  outline: none;
  font-size: 1rem;
  border-bottom: 2px solid #ccc;
  border-top: 2px solid transparent;
  transition: all 0.2s ease;
  border-radius: 0.2rem;
}

.input-field .dropdown {
  position: absolute;
  height: 3.2rem;
  min-height: 3rem;
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
.input-field .dropdown:is(:focus, :valid) {
  border-bottom-color: #4070f4 !important;
}
.input-field .dropdown:is(:focus, :valid) {
  color: #4070f4 !important;
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

@media screen and (max-width: 1100px) {
  .painel {
    flex-direction: column;
  }

  .painel-image {
    /* width: 100%;
    height: 50%; */
    display: none;
  }

  .painel-form {
    width: 100%;
    height: 50%;
  }
}
</style>
