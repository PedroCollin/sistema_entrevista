<template>
  <div class="painel">
    <toast position="top-right" />
    <div class="painel-image"></div>
    <div class="painel-form">
      <div class="form">
        <Steps :model="items" :readonly="true" style="margin-bottom: 1rem" />
        <keep-alive>
          <form>
            <div class="input-field">
              <Dropdown
                class="dropdown"
                v-model="vaga.curso"
                :options="cursos"
                option-value="code"
                optionLabel="name"
                placeholder="Selecione um curso"
              />
            </div>

            <div class="input-field">
              <input
                type="number"
                placeholder="Quantidade de vagas"
                v-model="vaga.quantidadeVaga"
                required
              />
            </div>

            <div class="datas">
              <h4>Data de abertura</h4>
              <div class="input-field">
                <input
                  type="date"
                  placeholder="Data de abertura"
                  v-model="vaga.dataAbertura"
                  required
                />
              </div>
              <h4>Data de fechamento</h4>
              <div class="input-field">
                <input
                  type="date"
                  placeholder="Data de fechamento"
                  v-model="vaga.dataFechamento"
                  required
                />
              </div>
            </div>
            <router-view
              :formData="formObject"
              @prevPage="prevPage($event)"
              @nextPage="nextPage($event)"
              @complete="complete"
            />
            <div class="button-bottom">
              <!-- <Button
                label="Registrar Vaga"
                class="p-button-raised p-button-success"
                @click="enviarVaga"
              ></Button> -->
            </div>
          </form>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCurso: null,
      cursos: [
        { name: 'Smart Automation', code: '1' },
        { name: 'Mecatronica', code: '2' },
        { name: 'Artes', code: '3' },
      ],
      vaga: {
        curso: '',
        quantidadeVaga: '',
        dataAbertura: '',
        dataFechamento: '',
      },
      items: [
        {
          label: 'Dados da Vaga',
          to: '/',
        },
        {
          label: 'Dinâmicas',
          to: '/vaga-dinamica',
        },
        {
          label: 'Confirmação',
          to: '/send-form',
        },
      ],
      formObject: {},
    }
  },
  methods: {
    nextPage(event) {
      for (let field in event.formData) {
        this.formObject[field] = event.formData[field]
      }

      this.$router.push(this.items[event.pageIndex + 1].to)
    },
    prevPage(event) {
      this.$router.push(this.items[event.pageIndex - 1].to)
    },
    complete() {
      this.$toast.add({
        severity: 'success',
        summary: 'Order submitted',
        detail:
          'Dear, ' +
          this.formObject.firstname +
          ' ' +
          this.formObject.lastname +
          ' your order completed.',
      })
    },
    async enviarVaga() {
      console.log('Vaga antes do POST')
      console.log(this.vaga)
      if (
        this.vaga.curso == '' ||
        this.vaga.quantidadeVaga == '' ||
        this.vaga.dataAbertura == '' ||
        this.vaga.dataFechamento == ''
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
            'http://127.0.0.1:8000/api/main/vaga/',
            {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              credentials: 'include',
              body: JSON.stringify([
                {
                  curso: this.vaga.curso,
                  quantidadeVaga: this.vaga.quantidadeVaga,
                  dataAbertura: this.vaga.dataAbertura,
                  dataFechamento: this.vaga.dataFechamento,
                  statusVaga: 1,
                },
              ]),
            }
          )
          console.log(responseToken)
          if (responseToken.status != '200') {
            this.$toast.add({
              severity: 'error',
              summary: 'Erro ao registrar nova vaga',
              detail: 'Error: ' + responseToken.status,
              life: 3000,
            })
          } else {
            this.$toast.add({
              severity: 'success',
              summary: 'Vaga cadastrada com sucesso',
              detail: 'Vaga registrada',
              life: 3000,
            })

            this.vaga.curso = ''
            this.vaga.dataAbertura = ''
            this.vaga.quantidadeVaga = ''
            this.vaga.dataFechamento = ''
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
  background-image: url('../../assets/images/bosch_logo_vaga.png');
  background-repeat: no-repeat center center;
  background-size: cover;
}

.painel-form {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 7.5rem;
  align-content: center;
  justify-content: center;
}

.button-bottom {
  display: flex;
  flex-direction: row;
  justify-content: right;
  align-content: top;
  margin-top: 10%;
}

/* --------------------------------------------------------------------------------- */

.form .input-field {
  position: relative;
  height: 35px;
  width: 100%;
  margin-top: 50px;
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

.datas {
  margin-top: 55px;
}

.datas .input-field {
  margin-top: 5px;
  margin-bottom: 40px;
}

.datas h4 {
  color: rgb(74, 74, 74);
  padding: 0.1rem;
}

::v-deep(b) {
  display: block;
}

::v-deep(.p-card-body) {
  padding: 2rem;
}

.p-steps .p-steps-item {
  background-color: #4070f4;
}

@media screen and (max-width: 1100px) {
  .painel-image {
    /* width: 100%;
    height: 50%; */
    display: none;
  }

  .painel-form {
    width: 100%;
    height: 80%;
  }

  .button-bottom {
    margin-top: 10%;
  }

  .button-bottom Button {
    font-size: 15px;
  }
}

@media screen and (max-width: 530px) {
  .painel-image {
    /* width: 100%;
    height: 50%; */
    display: none;
  }

  .painel-form {
    width: 100%;
    height: 80%;
    padding: 2rem;
    padding-top: 6rem;
  }

  .button-bottom {
    margin-top: 10%;
  }

  .button-bottom Button {
    font-size: 15px;
  }

  .datas h4 {
    margin-top: 10px;
    font-size: 16px;
  }
  .form .input-field {
    position: relative;
    height: 35px;
    margin-top: 2rem;
  }

  .datas .input-field {
    margin-top: 5px;
    margin-bottom: 40px;
  }
}
</style>
