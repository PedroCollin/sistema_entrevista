<template>
  <div class="container">
    <toast position="top-right" />

    <div class="form">
      <form>
        <div class="input-field">
          <input
            type="text"
            placeholder="Nome da dinâmica"
            v-model="dinamica.titulo"
            required
          />
        </div>
        <div class="input-field">
          <input
            type="time"
            step="2"
            class="time"
            v-model="dinamica.duracao"
            required
          />
        </div>
        <Divider />

        <span class="desc">
          <Textarea
            id="textarea"
            v-model="dinamica.descricao"
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
                v-model="criterio"
                required
              />
            </div>
            <Divider class="dividerCri" layout="vertical" />

            <div class="input-field">
              <input
                type="number"
                placeholder="Peso da dinâmica"
                v-model="peso"
                required
              />
            </div>
            <Button
              label="Adicionar"
              class="p-button-success p-button-text"
              @click="addCriterio"
            ></Button>
          </div>
          <Divider />
          <DataTable
            :value="criterios"
            responsiveLayout="scroll"
            :scrollable="true"
            scrollHeight="150px"
          >
            <Column
              v-for="col of columns"
              :field="col.field"
              :header="col.header"
              :key="col.field"
            ></Column>
          </DataTable>
        </Panel>
        <Divider />
        <Button
          label="Registrar dinâmica"
          class="p-button-raised p-button-success"
          @click="enviarDinamica"
        ></Button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columns: [
        { field: 'criterio', header: 'Critério' },
        { field: 'peso', header: 'Peso' },
      ],
      criterios: [],
      dinamica: {
        titulo: null,
        descricao: null,
        duracao: null,
        lista_criterios: {},
      },
      criterio: null,
      peso: null,
    }
  },
  // mounted() {
  //   this.$toast.add({severity:'success', summary: 'Success Message', detail:'Order submitted', life: 3000});
  // },
  methods: {
    addCriterio() {
      if (this.criterio != null || this.peso != null) {
        this.criterios.push({
          criterio: this.criterio,
          peso: this.peso,
        })
        for (let index = 0; index < this.criterios.length; index++) {
          this.dinamica.lista_criterios[this.criterios[index].criterio] =
            this.criterios[index].peso
        }
        this.criterio = null
        this.peso = null
        console.log(this.dinamica.lista_criterios)
        this.$toast.add({
          severity: 'success',
          summary: 'Criterio inserido com sucesso',
          detail: 'Criterio adicionado',
          life: 3000,
        })
      } else {
        this.$toast.add({
          severity: 'warn',
          summary: 'Prencha o campo de criterio e peso',
          detail: 'Todos os campos são necessarios',
          life: 3000,
        })
      }
    },
    async enviarDinamica() {
      try {
        const responseToken = await fetch(
          'http://127.0.0.1:8000/api/main/dinamica/',
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({
              titulo: this.dinamica.titulo,
              descricao: this.dinamica.descricao,
              duracao: this.dinamica.duracao,
              lista_criterios: this.dinamica.lista_criterios,
            }),
          }
        )
        if (responseToken.status != '200') {
          this.$toast.add({
            severity: 'error',
            summary: 'Erro ao registrar nova dinâmica',
            detail: 'Error: ' + responseToken.status,
            life: 3000,
          })
        } else {
          this.$toast.add({
            severity: 'success',
            summary: 'Dinâmica cadastrada com sucesso',
            detail: 'Dinâmica registrada',
            life: 3000,
          })
        }
        console.log(responseToken)
        console.log(this.dinamica)
      } catch (error) {
        this.$toast.add({
          severity: 'error',
          summary: 'Erro ao registrar nova dinâmica',
          detail: 'Erro: ' + error,
          life: 3000,
        })
      }
    },
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
  height: 100%;
  justify-content: center;
  align-items: center;
  padding: 5vh;
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

.p-button-success {
  width: 30%;
  height: 5vh;
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
  border-radius: 0.2rem;
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

@media screen and (max-width: 1400px) {
  .addCriterio {
    flex-direction: column;
  }

  .dividerCri {
    display: none;
  }
}

@media screen and (max-width: 600px) {
  .p-button-raised {
    height: 3rem;
    width: 8rem;
    font-size: 10pt;
  }
}
</style>
