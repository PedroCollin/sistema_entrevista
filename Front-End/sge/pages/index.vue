<template>
  <div class="carrossel">
    <Carousel :value="cursosObj" :numVisible="3" :numScroll="3" :responsiveOptions="responsiveOptions">
      <template #header>
          <h2>Cursos Cadastrados</h2>
      </template>
      <template #item="slotProps">
          <div class="product-item">
              <div class="product-item-content">
                  <div class="mb-3">
                      <img :src="'demo/images/product/' + slotProps.curso.titulo" :alt="slotProps.curso.titulo" class="imagem-curso" />
                  </div>
                  <div>
                      <h4 class="mb-1">{{slotProps.curso.titulo}}</h4>
                      <h6 class="mt-0 mb-3">${{slotProps.curso.descricao}}</h6>
                      <div class="car-buttons mt-5">
                          <Button icon="pi pi-search" class="p-button p-button-rounded mr-2" />
                          <Button icon="pi pi-star-fill" class="p-button-success p-button-rounded mr-2" />
                          <Button icon="pi pi-cog" class="p-button-help p-button-rounded" />
                      </div>
                  </div>
              </div>
          </div>
      </template>
    </Carousel>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  layout: 'default',
  data() {
    return {
      auth: false,
      user:"",
      cursosObj: [],
      responsiveOptions: [
        {
          breakpoint: '1024px',
          numVisible: 3,
          numScroll: 3
        },
        {
          breakpoint: '600px',
          numVisible: 2,
          numScroll: 2
        },
        {
          breakpoint: '480px',
          numVisible: 1,
          numScroll: 1
        }
		  ]
    };
  },
  async mounted() {
   
    this.$nuxt.$on("auth", (auth) => {
      this.auth = auth;
    });
    
    this.user = this.$store.state.user_session
  },
  created(){
    if(this.$store.state.user_session.id != null) {
      this.auth = true
    }
    else{
      this.$router.push('/auth/login/');
    }
  },
  computed: {
    ...mapState({
        user_session: (state) => state.user_session,
        token: (state) => state.token,
    }),
  },
  methods: {
    async logout() {
      await fetch("http://127.0.0.1:8000/api/logout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });
      this.auth = false;
      this.$store.commit("STORE_SESSION", {});
      this.$store.commit("STORE_TOKEN", {});
      await this.$router.push("/auth/login/");
    },
    
    async getCursos() {
      const response = await fetch("http://127.0.0.1:8000/api/main/curso");
      const data = await response.json();
      this.cursosObj = data.map((curso) => {
        return {
          id: curso.id,
          titulo: curso.titulo,
          descricao: curso.descricao,
          periodo: curso.periodo,
          carga_horaria: curso.carga_horaria,
          imgCurso: curso.imgCurso,
        };
      });
      return cursosObj;
    },

    // async cursos(){
    //   const response = await this.$http.get('/api/cursos');
    //   const cursos = response.data;
    //   const cursosObj = cursos.map(curso => {
    //     return {
    //       titulo: curso.titulo,
    //       descricao: curso.descricao,
    //       periodo: curso.periodo,
    //       carga_horaria: curso.carga_horaria,
    //     };
    //   });
    //   return cursosObj;
    // },
  },
};
</script>

<style scoped>

.container{
  background-color: rgb(248, 248, 248);
  align-content: center;
  justify-content: center;
}

.all{ 
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-left: 45%;
}

.p-carousel {
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-top: 8vh;
}

</style>
