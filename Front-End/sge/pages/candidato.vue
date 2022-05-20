<template>
 
    <div class="container">
      <div class="tabela">
      <DataTable
        :value="candidates"
        rowGroupMode="subheader"
        groupRowsBy="usuario.nome"
        sortMode="single"
        sortField="usuario.name"
        :sortOrder="1"
        responsiveLayout="scroll"
        :expandableRowGroups="true"
        :expandedRowGroups.sync="expandedRowGroups"
        @rowgroup-expand="onRowGroupExpand"
        @rowgroup-collapse="onRowGroupCollapse"
      >
        <Column field="DINÂMICA" header="DINÂMICA">
          <template #body="slotProps">
            <p style="text-align:center; width:100%">
              {{ slotProps.data.vagaDinamica.dinamica.titulo }}
            </p>
          </template>
        </Column>
        <Column
          v-for="(criterio, index) in list_criterios"
          :key="index"
          :field="criterio.toUpperCase()"
          :header="criterio.toUpperCase()"
        >
          <template #body="slotProps">
           <center>
              <p style="text-align:center; width:100%">
                {{ slotProps.data.list_criterios[criterio] }}
             </p>
           </center>
          </template>
        </Column>

        <template #groupheader="slotProps">
          <strong
            ><span class="image-text">
              {{ slotProps.data.usuario.nome }}
            </span></strong
          >
        </template>

        <template #body="slotProps">
          <p style="text-align:center; width:100%">
            {{ slotProps.data.list_criterios[criterio] }}
          </p>
        </template>

        <template #groupfooter="slotProps">

          <div class="ultima">
            <td colspan="4" style="text-align: left">OBSERVAÇÔES :</td> 
              <div class="final">
              <Textarea v-model="observacao" :autoResize="true" rows="5" cols="30" disabled/>
              </div>
            <div class="final">
            <td colspan="4" style="text-align: right">NOTA FINAL :</td>
              <td>{{
                    slotProps.data.nota
                  }}
            </td>
            </div>

          </div>

        </template> 
      </DataTable>
      </div>
       <div class="master">
    </div>
  </div>
</template>

<script>


export default {
   data() {
    return {
      list_criterios: [],
      candidates: [],
      expandedRowGroups: null,
      observacao: [],
    }
  },
  created() {
    this.$axios
      .get('http://127.0.0.1:8000/api/main/respostaDinamica/1')
      .then((response) => {
        // console.log(response.data[0])
        this.candidates.push(response.data[2])
        console.log('Candidates', this.candidates)
        this.observacao.push(response.data[2].observacao)
        console.log('observacao', this.observacao)
        this.list_criterios = Object.keys(response.data[2].list_criterios)
        console.log('criterios', this.list_criterios)

      })
  },
  methods: {
    onRowGroupExpand(event) {},
    onRowGroupCollapse(event) {},
    calculateCustomerTotal(name) {
      let total = 0
      if (this.customers) {
        for (let customer of this.customers) {
          if (customer.representative.name === name) {
            total++
          }
        }
      }
      return total
    },
  },
};
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

.tabela{
  overflow-x:auto;
}

.final{
  padding-top: 20px;
}

.ultima{
  width: 100%;
  padding: 30px;
  
}
.master{
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #ebebeb;
}
.p-column-header-content{
  display: contents !important;
  text-align: center !important;

}
</style>
