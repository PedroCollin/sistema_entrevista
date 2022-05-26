<template>
  <div class="painel">
    <toast position="top-right" />
    <div class="painel-image"></div>
    <div class="painel-form">
      <div class="stepper">
        <div class="stepper-progress">
          <div
            class="stepper-progress-bar"
            :style="'width:' + stepperProgress"
          ></div>
        </div>

        <div
          class="stepper-item"
          :class="{ current: step == item, success: step > item }"
          v-for="item in 3"
          :key="item"
        >
          <div class="stepper-item-counter">
            <img class="icon-success" alt="" src="" />
            <span class="number">{{ item }}</span>
          </div>
          <span class="stepper-item-title">{{
            lista_titulo_step[item - 1]
          }}</span>
        </div>
      </div>

      <div class="steps" v-for="item in 3" :key="item">
        <div class="form" v-if="step == item">
          <form>
            <div class="step-01" v-if="item == 1">
              <div class="input-field">
                <Dropdown
                  class="dropdown"
                  v-model="vaga.curso"
                  :options="cursos"
                  option-value="id"
                  optionLabel="titulo"
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
            </div>

            <div class="step-02" v-if="item == 2">
              <PickList v-model="products" dataKey="titulo" class="picklist">
                <template #sourceheader> Disponivel </template>
                <template #targetheader> Selecionado </template>
                <template #item="slotProps">
                  <div class="p-caritem">
                    <div>
                      <span class="p-caritem-vin">{{
                        slotProps.item.titulo
                      }}</span>
                      <span> {{ slotProps.item.duracao }}</span>
                    </div>
                  </div>
                </template>
              </PickList>
            </div>

            <div class="step-03" v-if="item == 3">
              <DataTable :value="[vaga]" responsiveLayout="scroll">
                <Column
                  v-for="col of columns_dados_vaga"
                  :field="col.field"
                  :header="col.header"
                  :key="col.field"
                ></Column>
              </DataTable>

              <Divider />

              <DataTable
                :value="products[1]"
                scrollable
                scrollHeight="400px"
                :virtualScrollerOptions="{ itemSize: 46 }"
              >
                <Column
                  field="titulo"
                  header="Titulo"
                  style="min-width: '200px'"
                ></Column>
                <Column
                  field="duracao"
                  header="Duração"
                  style="min-width: '200px'"
                ></Column>
              </DataTable>
            </div>

            <div class="button-bottom">
              <Button
                label="Anterior"
                class="p-button-raised p-button-secondary"
                @click="step--"
                :disabled="step == 1"
              ></Button>
              <Button
                v-if="item != 3"
                label="Seguinte"
                class="p-button-raised p-button-primary"
                @click="step++"
              ></Button>
              <Button
                v-if="item == 3"
                label="Registrar vaga"
                class="p-button-raised p-button-success"
                @click="enviarVaga"
              ></Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedCurso: null,
      cursos: [],
      products: [[], []],
      vaga: {
        curso: '',
        quantidadeVaga: '',
        dataAbertura: '',
        dataFechamento: '',
      },
      columns_dados_vaga: null,
      step: 1,
      lista_titulo_step: ['Dados da Vaga', 'Dinâmicas', 'Confirmar Dados'],
    }
  },
  created() {
    ;(this.columns_dados_vaga = [
      { field: 'curso', header: 'Curso' },
      { field: 'quantidadeVaga', header: 'Vagas' },
      { field: 'dataAbertura', header: 'Data abertura' },
      { field: 'dataFechamento', header: 'Data final' },
    ]),
      this.$axios.$get('main/curso').then((response) => {
        this.cursos = response
      }),
      this.$axios.$get('main/dinamica').then((response) => {
        this.products[0] = response
      })
  },
  computed: {
    stepperProgress() {
      return (100 / 2) * (this.step - 1) + '%'
    },
  },
  methods: {
    enviarVaga: async function () {
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
          const vaga = await responseToken.json()

          if (responseToken.status != '200') {
            this.$toast.add({
              severity: 'error',
              summary: 'Erro ao registrar nova vaga',
              detail: 'Error: ' + responseToken.status,
              life: 3000,
            })
          } else {
            for (const key in this.products[1]) {
              const dinamica = this.products[1][key]
              const responseTokenDinamica = await fetch(
                'http://127.0.0.1:8000/api/main/vagaDinamica/',
                {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  credentials: 'include',
                  body: JSON.stringify([
                    {
                      vaga: vaga[0].id,
                      dinamica: dinamica.id,
                    },
                  ]),
                }
              )
            }
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

            this.products[1] = []
            this.step = 1
          }
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

<style lang="scss" scoped>
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
  justify-content: space-between;
  align-content: top;
  margin-top: 10%;

  .p-button-primary {
    background-color: #4070f4;
    border: 1px solid #4070f4;
  }

  .p-button-primary:hover {
    background: #2e5fe7 !important;
    color: #fff;
    border-color: #2e5fe7 !important;
    border: none;
  }

  .p-button-secondary {
    background-color: #e0e0e0;
    border: 1px solid #e0e0e0;
    color: #5c5c5c;
  }

  .p-button-secondary:hover {
    background: #c0c0c0 !important;
    color: #3f3f3f;
    border-color: #c0c0c0 !important;
    border: none;
  }

  &:disabled {
    opacity: 0.3;
    pointer-events: none;
  }
}

/* --------------------------------------------------------------------------------- */

.picklist {
  margin-top: 50px;
}

// ---------------------------------

.form {
  .input-field {
    position: relative;
    height: 35px;
    width: 100%;
    margin-top: 50px;
  }
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

.stepper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 85%;
  position: relative;
  z-index: 0;
  margin-top: 1rem;
  margin-bottom: 20px;
  margin-left: 7%;

  &-progress {
    position: absolute;
    background-color: rgb(121, 121, 121);
    height: 2px;
    z-index: -1;
    left: 0;
    right: 0;
    margin: 0 auto;

    &-bar {
      position: absolute;
      left: 0;
      height: 100%;
      width: 0%;
      background-color: #4070f4;
      transition: all 500ms ease;
    }
  }
}

.stepper-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: rgb(121, 121, 121);
  transition: all 500ms ease;

  &-counter {
    height: 50px;
    width: 50px;
    display: grid;
    place-items: center;
    background-color: #fff;
    border-radius: 100%;
    border: 2px solid rgb(121, 121, 121);
    position: relative;

    .icon-success {
      position: absolute;
      opacity: 0;
      transform: scale(0);
      width: 24px;
      transition: all 500ms ease;
    }
    .number {
      font-size: 22px;
      transition: all 500ms ease;
    }
  }

  &-title {
    display: flex;
    position: absolute;
    justify-content: center;
    font-size: 18px;
    bottom: -24px;
    width: 25%;
  }
}

.stepper-item.success {
  .stepper-item-counter {
    border-color: #4070f4;
    background-color: #d4deff;
    color: #fff;
    font-weight: 600;

    .icon-success {
      opacity: 1;
      transform: scale(1);
    }

    .number {
      opacity: 0;
      transform: scale(0);
    }
  }

  .stepper-item-title {
    color: #4070f4;
  }
}

.stepper-item.current {
  .stepper-item-counter {
    border-color: #4070f4;
    background-color: #d4deff;
    color: #4070f4;
    font-weight: 600;

    .stepper-item-title {
      color: #4070f4 !important;
    }
  }
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
