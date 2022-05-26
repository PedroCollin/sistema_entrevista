<template>
  <div class="mainContent">
    <div class="tituloCarrossel">
      <h3>VAGAS</h3>
    </div>
    <div class="carrossel">
      <Carousel :value="cursosObj" :numVisible="3" :numScroll="3" :circular="true" :responsiveOptions="responsiveOptions">
        <template #item="slotProps">
            <div class="product-item">
                <div class="product-item-content">
                    <div class="mb-3">
                        <img src="../assets/images/manufacture_like_a_bosch_1.jpg" width="480px" height="420px"/>
                    </div>
                    <div class="cardCursos">
                        <h4 class="mb-1">{{slotProps.data.curso.titulo}}</h4>
                        <h6 class="mt-0 mb-3">{{slotProps.data.curso.titulo}}</h6>
                        <div class="car-buttons mt-5">
                            <NuxtLink :to="'/vaga/candidatos/' + slotProps.data.id"><Button class="p-button-danger mr-2">Candidatos</Button></NuxtLink>
                            <Button class="p-button mr-2">Dinâmicas</Button>
                            <Button class="p-button-success">Entrevista</Button>
                        </div>
                    </div>
                </div>
            </div>
        </template>
      </Carousel>
    </div>
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
    this.$axios.$get('main/vaga').then((response) => {
        this.cursosObj = response
        console.log(this.cursoObj)
    })
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
    }
  },
};
</script>

<style >

.product-item .product-item-content {
  border: 1px solid var(--surface-border);
  border-radius: 3px;
  margin: .3rem;
  text-align: center;
  padding: 2rem 0;
}

.product-item .product-image {
  width: 50%;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)
}

.carrossel {
  margin-top:8px;
  margin-bottom: 47px;
}

.tituloCarrossel {
  justify-content: center;
  align-content: center;
  align-items: center;
  text-align: center;
  margin-top: 25px;
  margin-bottom: 35px;
  font-family: 'Roboto', sans-serif;
  font-size: 1.5rem;

}

</style>
