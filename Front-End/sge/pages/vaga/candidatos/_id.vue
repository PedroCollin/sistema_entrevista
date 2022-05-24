<template>
  <div class="container">
    <div class="all" v-if="auth">
      <!-- START -->
      <div class="card">
        <Toolbar class="mb-4">
          <template #start>
            <Button
              label="New"
              icon="pi pi-plus"
              class="p-button-success mr-2"
              @click="openNew"
            />
            <Button
              label="Delete"
              icon="pi pi-trash"
              class="p-button-danger"
              @click="confirmDeleteSelected"
              :disabled="!selectedCandidatos || !selectedCandidatos.length"
            />
          </template>

          <template #end>
            <FileUpload
              mode="basic"
              accept=".csv"
              :maxFileSize="1000000"
              label="Import"
              chooseLabel="Import"
              class="mr-2 inline-block"
              :customUpload="true"
              @uploader="myUploader"
            />
            <Button
              label="Export"
              icon="pi pi-upload"
              class="p-button-help"
              @click="exportCSV($event)"
            />
          </template>
        </Toolbar>

        <DataTable
          ref="dt"
          :value="candidatos"
          :selection.sync="selectedCandidatos"
          dataKey="id"
          :paginator="true"
          :rows="5"
          :filters="filters"
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rowsPerPageOptions="[5, 10, 15]"
          currentPageReportTemplate="Pagina {first} de {last} de total de {totalRecords} candidatos"
          responsiveLayout="scroll"
        >
          <template #header>
            <div
              class="table-header flex flex-column md:flex-row md:justiify-content-between"
            >
              <h2 class="mb-2 md:m-0 p-as-md-center">Gerenciar Candidatos</h2>
              <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText
                  v-model="filters['global'].value"
                  placeholder="Search..."
                />
              </span>
            </div>
          </template>

          <Column
            selectionMode="multiple"
            style="width: 3rem"
            :exportable="false"
          ></Column>
          <Column
            field="nome"
            header="Nome"
            :sortable="true"
            style="min-width: 16rem"
          ></Column>
          <Column header="Image">
            <template #body="slotProps">
              <img
                src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
                :alt="slotProps.data.image"
                class="product-image"
              />
            </template>
          </Column>
          <Column
            field="email"
            header="Email"
            :sortable="true"
            style="min-width: 8rem"
          >
            <!-- <template #body="slotProps">
              {{ formatCurrency(slotProps.data.email) }}
            </template> -->
          </Column>
          <Column
            field="cpf"
            header="CPF"
            :sortable="true"
            style="min-width: 10rem"
          ></Column>
          <Column
            field="rg"
            header="RG"
            :sortable="true"
            style="min-width: 10rem"
          ></Column>
          <!-- <Column
            field="rating"
            header="Reviews"
            :sortable="true"
            style="min-width: 12rem"
          >
            <template #body="slotProps">
              <Rating
                :modelValue="slotProps.data.rating"
                :readonly="true"
                :cancel="false"
              />
            </template>
          </Column> -->
          <Column :exportable="false" style="min-width: 8rem">
            <template #body="slotProps">
              <Button
                icon="pi pi-pencil"
                class="p-button-rounded p-button-success mr-2"
                @click="editCandidato(slotProps.data)"
              />
              <Button
                icon="pi pi-trash"
                class="p-button-rounded p-button-warning"
                @click="confirmDeleteCandidato(slotProps.data)"
              />
            </template>
          </Column>
        </DataTable>
      </div>

      <Dialog
        :visible.sync="candidatoDialog"
        :style="{ width: '450px' }"
        header="Product Details"
        :modal="true"
        class="p-fluid"
      >
        <img
          src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
          :alt="candidato.image"
          class="product-image"
          v-if="candidato.image"
        />
        <div class="field">
          <label for="nome">Nome</label>
          <InputText
            id="nome"
            v-model="candidato.nome"
            required="true"
            autofocus
            :class="{ 'p-invalid': submitted && !candidato.nome }"
          />
          <small class="p-error" v-if="submitted && !candidato.nome"
            >Nome é obrigatorio.</small
          >
        </div>
        <div class="field">
          <label for="email">Email</label>
          <InputText id="email" v-model="candidato.email" required="true" />
        </div>

        <div class="field">
          <label for="rg">RG</label>
          <InputText id="rg" v-model="candidato.rg" required="true" />
        </div>

        <div class="field">
          <label for="cpf">CPF</label>
          <InputText id="cpf" v-model="candidato.cpf" required="true" />
        </div>

        <div class="field">
          <label for="cidade" class="mb-3">Cidade</label>
          <Dropdown
            id="inventoryStatus"
            v-model="candidato.cidade"
            :options="cidades"
            optionLabel="nome"
            placeholder="Selecione uma cidade"
          >
          </Dropdown>
        </div>

        <template #footer>
          <Button
            label="Cancel"
            icon="pi pi-times"
            class="p-button-text"
            @click="hideDialog"
          />
          <Button
            label="Save"
            icon="pi pi-check"
            class="p-button-text"
            @click="saveCandidato"
          />
        </template>
      </Dialog>

      <Dialog
        :visible.sync="deleteCandidatoDialog"
        :style="{ width: '450px' }"
        header="Confirm"
        :modal="true"
      >
        <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="candidato"
            >Tem certeza que deseja deletar este candidato
            <b>{{ candidato.nome }}</b
            >?</span
          >
        </div>
        <template #footer>
          <Button
            label="No"
            icon="pi pi-times"
            class="p-button-text"
            @click="deleteCandidatoDialog = false"
          />
          <Button
            label="Yes"
            icon="pi pi-check"
            class="p-button-text"
            @click="deleteCandidato(candidato.id)"
          />
        </template>
      </Dialog>

      <Dialog
        :visible.sync="deleteCandidatosDialog"
        :style="{ width: '450px' }"
        header="Confirm"
        :modal="true"
      >
        <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="candidato"
            >Tem certeza que deseja deletar o candidato selecionado?</span
          >
        </div>
        <template #footer>
          <Button
            label="No"
            icon="pi pi-times"
            class="p-button-text"
            @click="deleteCandidatosDialog = false"
          />
          <Button
            label="Yes"
            icon="pi pi-check"
            class="p-button-text"
            @click="deleteSelectedCandidatos"
          />
        </template>
      </Dialog>
      <!-- END -->
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { FilterMatchMode } from 'primevue/api'
import imageCompression from "browser-image-compression";

export default {
  layout: 'default',
  data() {
    return {
      auth: false,
      user: '',
      candidatos: [],
      candidatoDialog: false,
      deleteCandidatoDialog: false,
      deleteCandidatosDialog: false,
      candidato: {},
      filters: {},
      bool_editCandidato: false,
      selectedCandidatos: null,
      submitted: false,
      fileCSV: null,
      idVaga: 0,
      cidades: [
        { nome: 'Campinas', id: '0' },
        { nome: 'Sumare', id: '1' },
        { nome: 'Indaiatuba', id: '2' },
      ],
    }
  },
  async mounted() {
    this.$nuxt.$on('auth', (auth) => {
      this.auth = auth
    })
    this.idVaga = this.$route.fullPath.replace(/^\D+/g, '')
    // console.log(this.$route.params.slug)
    console.log(this.idVaga)

    this.user = this.$store.state.user_session

    this.$axios.$get('main/candidato/' + this.idVaga).then((response) => {
      this.candidatos = response
      console.log(response)
    })
  },
  created() {
    this.initFilters()
    if (this.$store.state.user_session.id != null) {
      this.auth = true
    } else {
      this.$router.push('/auth/login/')
    }
  },
  computed: {},
  methods: {
    formatCurrency(value) {
      if (value)
        return value.toLocaleString('en-US', {
          style: 'currency',
          currency: 'USD',
        })
      return
    },
    openNew() {
      console.log('open')
      this.candidato = {}
      this.submitted = false
      this.candidatoDialog = true
    },
    hideDialog() {
      this.candidatoDialog = false
      this.submitted = false
      this.bool_editProduct = false
    },
    saveCandidato() {
      this.submitted = true
      console.log(this.candidatos)
      if (this.candidato.nome) {
        if (this.bool_editCandidato) {
          this.candidatos[this.findIndexById(this.candidato.id)] =
            this.candidato

          this.$axios
            .put('main/candidato/' + this.candidato.id + '/', {
              nome: this.candidato.nome,
              email: this.candidato.email,
              rg: this.candidato.rg,
              cpf: this.candidato.cpf,
              cidade: this.candidato.cidade.id,
              vaga: this.idVaga,
            })
            .then(function (response) {
              console.log(response)
            })
            .catch(function (error) {
              console.log(error)
            })

          this.$toast.add({
            severity: 'success',
            summary: 'Successful',
            detail: 'Candidato Atualizado',
            life: 5000,
          })
        } else {
          this.candidato.image = 'products-placeholder.svg'
          this.candidato.vaga = this.idVaga
          this.candidato.cidade = this.candidato.cidade
          this.candidatos.push(this.candidato)

          this.$axios
            .post('main/candidato/', [
              {
                nome: this.candidato.nome,
                email: this.candidato.email,
                rg: this.candidato.rg,
                cpf: this.candidato.cpf,
                cidade: this.candidato.cidade.id,
                vaga: this.candidato.vaga,
              },
            ])
            .then(function (response) {
              console.log(response)
            })
            .catch(function (error) {
              console.log(error)
            })

          this.$toast.add({
            severity: 'success',
            summary: 'Successful',
            detail: 'Candidato Registrado',
            life: 5000,
          })
        }
        this.candidatoDialog = false
        this.candidato = {}
      }
    },
    editCandidato(candidato) {
      this.candidato = { ...candidato }
      this.candidatoDialog = true
      this.bool_editCandidato = true
    },
    confirmDeleteCandidato(candidato) {
      this.candidato = candidato
      this.deleteCandidatoDialog = true
    },
    deleteCandidato(id) {
      console.log('ID: ' + id)
      this.candidatos = this.candidatos.filter(
        (val) => val.id !== this.candidato.id
      )
      this.deleteCandidatoDialog = false
      this.candidato = {}

      this.$axios
        .delete('main/candidato/' + id + '/')
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })

      this.$toast.add({
        severity: 'success',
        summary: 'Successful',
        detail: 'Candidato Deletado',
        life: 5000,
      })
    },
    findIndexById(id) {
      let index = -1
      for (let i = 0; i < this.candidatos.length; i++) {
        if (this.candidatos[i].id === id) {
          index = i
          break
        }
      }

      return index
    },
    exportCSV() {
      this.$refs.dt.exportCSV()
    },
    confirmDeleteSelected() {
      this.deleteCandidatosDialog = true
    },
    deleteSelectedCandidatos() {
      this.candidatos = this.candidatos.filter(
        (val) => !this.selectedCandidatos.includes(val)
      )

      for (const key in this.selectedCandidatos) {
        console.log(this.selectedCandidatos[key])
        this.$axios
          .delete('main/candidato/' + this.selectedCandidatos[key].id + '/')
          .then(function (response) {
            console.log(response)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
      this.deleteCandidatosDialog = false
      this.selectedCandidatos = null
      this.$toast.add({
        severity: 'success',
        summary: 'Successful',
        detail: 'Candidatos Deletado',
        life: 3000,
      })
    },
    initFilters() {
      this.filters = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      }
    },
    myUploader(event) {
      const fileEvent = event.files[0];

      const fileZiseMb = fileEvent.size / 1024 / 1024;
      if (fileZiseMb > 4.5) {
        const options = {
          maxSizeMB: 4,
          maxWidthOrHeight: 1920,
          useWebWorker: true,
        };
        try {
          const compressedFile = imageCompression(
            fileEvent,
            options
          );
          console.log(
            "compressedFile instanceof Blob",
            compressedFile instanceof Blob
          );
          console.log(
            `compressedFile size ${compressedFile.size / 1024 / 1024} MB`
          );
          this.fileCSV = compressedFile;
        } catch (error) {
          console.log(error);
          this.$toast.add({severity:'error', summary: 'Erro ao Compactar Img!', life: 3500});;
        }
      } else {
        //FILE DOESN'T NEED TO BE COMPRESSED
        this.fileCSV = fileEvent;
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  background-color: rgb(248, 248, 248);
  align-content: center;
  justify-content: center;
}

.all {
  justify-content: center;
  align-content: center;
  align-items: center;
}

// ------------------------------------------------------------ PRIMEVUE
.table-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  @media screen and (max-width: 960px) {
    align-items: start;
  }
}

.product-image {
  width: 50px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}

.p-dialog .product-image {
  width: 50px;
  margin: 0 auto 2rem auto;
  display: block;
}

.confirmation-content {
  display: flex;
  align-items: center;
  justify-content: center;
}
@media screen and (max-width: 960px) {
  ::v-deep(.p-toolbar) {
    flex-wrap: wrap;

    .p-button {
      margin-bottom: 0.25rem;
    }
  }
}
</style>
