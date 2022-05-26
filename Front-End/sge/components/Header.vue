<template>
    <div class="mainDiv">
        <header class="header"></header>
        <div class="subHeader">
            <a class="ignore-css" href="../../">
                <img class="BoschLogo" src="../assets/images/BoschLogo.png" alt="Logo Bosch">
            </a>
            <div class="subDiv">

                <Sidebar :visible.sync="visibleRight" position="right">
                    <a href="../../" class="py-5 px-3">
                        <img class="HomeIcon" src = "../assets/images/house-solid.svg" alt="HomeIcon" width="20" height="15"/>
                        HOME
                    </a><br><br><br>
                    <h3>Cadastros</h3><br>
                    <a href="../../auth/register" class="py-5 px-3">Cadastrar Usuário</a><br><br><br>
                    <a href="../../curso" class="py-5 px-3">Cadastrar Curso</a><br><br><br>
                    <a href="../../dinamica" class="py-5 px-3">Cadastrar Dinâmica</a><br><br><br>
                    <a href="../../vaga/" class="py-5 px-3">Cadastrar Vaga</a><br><br><br><br>
                    <h3>Informações / Dúvidas</h3><br>
                    <a href="../../sobre" class="py-5 px-3">Sobre o Sistema</a><br><br><br><br><br><br><br><br><br><br><br><br>
                    <a href="../../auth/login" class="py-5 px-3" @click="logout">SAIR</a>
                </Sidebar>

                <Button icon="pi pi-bars" @click="visibleRight = true" />
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    props: [""],
    
    data() {
        return {
            visibleRight: false,
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
        await fetch("http://127.0.0.1:8000/api/logout/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
        });
        this.auth = false;
        this.$store.commit("STORE_SESSION", {});
        this.$store.commit("STORE_TOKEN", {});
        await this.$router.push("/auth/login/");
        },
    },
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');


.py-5.px-3, .py-5.px-3:hover, .py-5.px-3:focus, .py-5.px-3:active, .py-5.px-3:hover img {
    text-decoration: none;
    color: inherit;
 }

.py-5.px-3:hover {
    color: red;
}

.py-5.px-3:hover img{   
    transform: scale(1.5);
}

.HomeIcon {
    margin-right: 10px;
}

.header {
    width: 100%;
    min-width: 430px;
    background: url('http://thomasantonbinder.com/code/wp-content/uploads/Bosch-Supergraphic.jpg');
    background-size: cover;
    left: 0;
    top: 0;
    right: 0;
    height: 0.7rem;
    display: flex;
}

.BoschLogo {
    margin-left: 1rem;
    min-width: 10.5rem;
    height: 2.5625rem;
    margin-right: 55%;
}

.subHeader {
    display: flex;
    align-items: center;
    margin-top: 0.7rem;
    margin-bottom: 0.65rem;
    
}

@media only screen and (max-width: 1456px) {
    
}

.subDiv {
    margin-right: 1rem;
    font-family: 'Roboto', sans-serif;
    font-size: 1.1rem;
    border: none;
    margin-left: auto;
}

.mainDiv {
    height: 75px;
    border-bottom: 1px solid rgb(238, 238, 238);
    background-color: #ffffff;
}

</style>