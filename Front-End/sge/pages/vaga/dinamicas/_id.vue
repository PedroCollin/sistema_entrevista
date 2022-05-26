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
              :disabled="!selectedDinamicas || !selectedDinamicas.length"
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
          :value="Dinamicas"
          :selection.sync="selectedDinamicas"
          dataKey="id"
          :paginator="true"
          :rows="5"
          :filters="filters"
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rowsPerPageOptions="[3, 5, 10]"
          currentPageReportTemplate="Pagina {first} de {last} de total de {totalRecords} Dinamicas"
          responsiveLayout="scroll"
        >
          <template #header>
            <div
              class="
                table-header
                flex flex-column
                md:flex-row md:justiify-content-between
              "
            >
              <h2 class="mb-2 md:m-0 p-as-md-center">Gerenciar Dinamicas</h2>
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
            field="titulo"
            header="Titulo"
            :sortable="true"
            style="min-width: 16rem"
          ></Column>
          <Column
            field="duracao"
            header="Duração"
            :sortable="true"
            style="min-width: 8rem"
          >
          </Column>
          <Column
            field="status"
            header="Status"
            :sortable="true"
            style="min-width: 10rem"
          ></Column>
          <Column :exportable="false" style="min-width: 8rem">
            <template #body="slotProps">
              <Button
                icon="pi pi-pencil"
                class="p-button-rounded p-button-success mr-2"
                @click="editDinamica(slotProps.data)"
              />
              <Button
                icon="pi pi-trash"
                class="p-button-rounded p-button-warning"
                @click="confirmDeleteDinamica(slotProps.data)"
              />
            </template>
          </Column>
        </DataTable>
      </div>

      <Dialog
        :visible.sync="DinamicaDialog"
        :style="{ width: '450px' }"
        header="Product Details"
        :modal="true"
        class="p-fluid"
      >
        <div class="field">
          <label for="titulo">Titulo</label>
          <InputText
            id="titulo"
            v-model="Dinamica.titulo"
            required="true"
            autofocus
            :class="{ 'p-invalid': submitted && !Dinamica.titulo }"
          />
          <small class="p-error" v-if="submitted && !Dinamica.titulo"
            >Titulo é obrigatorio.</small
          >
        </div>
        <div class="field">
          <label for="duracao">Duração</label>
          <InputText id="duracao" v-model="Dinamica.duracao" required="true" />
        </div>

        <div class="field">
          <label for="status">status</label>
          <InputText id="status" v-model="Dinamica.status" required="true" />
        </div>
        <!-- 
        <div class="field">
          <label for="cidade" class="mb-3">Cidade</label>
          <Dropdown
            id="inventoryStatus"
            v-model="Dinamica.cidade"
            :options="cidades"
            optionLabel="titulo"
            placeholder="Selecione uma cidade"
          >
          </Dropdown>
        </div> -->

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
            @click="saveDinamica"
          />
        </template>
      </Dialog>

      <Dialog
        :visible.sync="deleteDinamicaDialog"
        :style="{ width: '450px' }"
        header="Confirm"
        :modal="true"
      >
        <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="Dinamica"
            >Tem certeza que deseja deletar esta Dinamica
            <b>{{ Dinamica.titulo }}</b
            >?</span
          >
        </div>
        <template #footer>
          <Button
            label="No"
            icon="pi pi-times"
            class="p-button-text"
            @click="deleteDinamicaDialog = false"
          />
          <Button
            label="Yes"
            icon="pi pi-check"
            class="p-button-text"
            @click="deleteDinamica(Dinamica.id)"
          />
        </template>
      </Dialog>

      <Dialog
        :visible.sync="deleteDinamicasDialog"
        :style="{ width: '450px' }"
        header="Confirm"
        :modal="true"
      >
        <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="Dinamica"
            >Tem certeza que deseja deletar a dinâmica selecionada?</span
          >
        </div>
        <template #footer>
          <Button
            label="No"
            icon="pi pi-times"
            class="p-button-text"
            @click="deleteDinamicasDialog = false"
          />
          <Button
            label="Yes"
            icon="pi pi-check"
            class="p-button-text"
            @click="deleteSelectedDinamicas"
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
import imageCompression from 'browser-image-compression'

export default {
  layout: 'default',
  data() {
    return {
      auth: false,
      user: '',
      Dinamicas: [],
      DinamicaDialog: false,
      deleteDinamicaDialog: false,
      deleteDinamicasDialog: false,
      Dinamica: {},
      filters: {},
      bool_editDinamica: false,
      selectedDinamicas: null,
      submitted: false,
      fileCSV: null,
      idVaga: 0,
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

    this.$axios.$get('main/vagaDinamica/' + this.idVaga).then((response) => {
      const dinamicas = response.dinamica

      for (const key in dinamicas) {

        this.Dinamicas.push(dinamicas[key])
      }
      // console.log('teste: ')
      // console.log(this.Dinamicas.entries())
      // console.log(response)
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
    openNew() {
      console.log('open')
      this.Dinamica = {}
      this.submitted = false
      this.DinamicaDialog = true
    },
    hideDialog() {
      this.DinamicaDialog = false
      this.submitted = false
      this.bool_editProduct = false
    },
    saveDinamica() {
      this.submitted = true
      console.log(this.Dinamicas)
      if (this.Dinamica.titulo) {
        if (this.bool_editDinamica) {
          this.Dinamicas[this.findIndexById(this.Dinamica.id)] = this.Dinamica

          this.$axios
            .put('main/Dinamica/' + this.Dinamica.id + '/', {
              titulo: this.Dinamica.titulo,
              duracao: this.Dinamica.duracao,
              rg: this.Dinamica.rg,
              status: this.Dinamica.status,
              cidade: this.Dinamica.cidade.id,
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
            detail: 'Dinamica Atualizado',
            life: 5000,
          })
        } else {
          this.Dinamica.image = 'products-placeholder.svg'
          this.Dinamica.vaga = this.idVaga
          this.Dinamica.cidade = this.Dinamica.cidade
          this.Dinamicas.push(this.Dinamica)

          this.$axios
            .post('main/Dinamica/', [
              {
                titulo: this.Dinamica.titulo,
                duracao: this.Dinamica.duracao,
                rg: this.Dinamica.rg,
                status: this.Dinamica.status,
                cidade: this.Dinamica.cidade.id,
                vaga: this.Dinamica.vaga,
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
            detail: 'Dinamica Registrado',
            life: 5000,
          })
        }
        this.DinamicaDialog = false
        this.Dinamica = {}
      }
    },
    editDinamica(Dinamica) {
      this.Dinamica = { ...Dinamica }
      this.DinamicaDialog = true
      this.bool_editDinamica = true
    },
    confirmDeleteDinamica(Dinamica) {
      this.Dinamica = Dinamica
      this.deleteDinamicaDialog = true
    },
    deleteDinamica(id) {
      console.log('ID: ' + id)
      this.Dinamicas = this.Dinamicas.filter(
        (val) => val.id !== this.Dinamica.id
      )
      this.deleteDinamicaDialog = false
      this.Dinamica = {}

      this.$axios
        .delete('main/Dinamica/' + id + '/')
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })

      this.$toast.add({
        severity: 'success',
        summary: 'Successful',
        detail: 'Dinamica Deletado',
        life: 5000,
      })
    },
    findIndexById(id) {
      let index = -1
      for (let i = 0; i < this.Dinamicas.length; i++) {
        if (this.Dinamicas[i].id === id) {
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
      this.deleteDinamicasDialog = true
    },
    deleteSelectedDinamicas() {
      this.Dinamicas = this.Dinamicas.filter(
        (val) => !this.selectedDinamicas.includes(val)
      )

      for (const key in this.selectedDinamicas) {
        console.log(this.selectedDinamicas[key])
        this.$axios
          .delete('main/Dinamica/' + this.selectedDinamicas[key].id + '/')
          .then(function (response) {
            console.log(response)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
      this.deleteDinamicasDialog = false
      this.selectedDinamicas = null
      this.$toast.add({
        severity: 'success',
        summary: 'Successful',
        detail: 'Dinamicas Deletado',
        life: 3000,
      })
    },
    initFilters() {
      this.filters = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      }
    },
    myUploader(event) {
      const fileEvent = event.files[0]

      const fileZiseMb = fileEvent.size / 1024 / 1024
      if (fileZiseMb > 4.5) {
        const options = {
          maxSizeMB: 4,
          maxWidthOrHeight: 1920,
          useWebWorker: true,
        }
        try {
          const compressedFile = imageCompression(fileEvent, options)
          console.log(
            'compressedFile instanceof Blob',
            compressedFile instanceof Blob
          )
          console.log(
            `compressedFile size ${compressedFile.size / 1024 / 1024} MB`
          )
          this.fileCSV = compressedFile
        } catch (error) {
          console.log(error)
          this.$toast.add({
            severity: 'error',
            summary: 'Erro ao Compactar Img!',
            life: 3500,
          })
        }
      } else {
        //FILE DOESN'T NEED TO BE COMPRESSED
        this.fileCSV = fileEvent
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
