<template>
    <div>
        <header class="header"></header>
        <subheader class="subHeader">
            <img class="BoschLogo" src="../assets/images/BoschLogo.png" alt="Logo Bosch">
            <div class="subDiv">
                <a class="texto1" href="url" style="text-decoration:none; color: inherit">Cadastro de Entrevistador</a>
                <a class="texto2" href="url" style="text-decoration:none; color: inherit">Cadastro de Candidato</a>
            </div>
        </subheader>
    </div>
</template>

<script>
export default {
    name: "MainHeader"
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

.header {
    width: 100%;
    min-width: 430px;
    background: url('http://thomasantonbinder.com/code/wp-content/uploads/Bosch-Supergraphic.jpg');
    background-size: cover;
    left: 0;
    top: 0;
    right: 0;
    position: fixed;
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
    margin-top: 1.4rem;
    margin-bottom: 1.4rem;
}

@media only screen and (max-width: 1456px) {
    .subDiv {
        display: none;
    }
}

.subDiv {
    left: 600px;
    top: 2rem;
    margin-right: 1rem;
    font-family: 'Roboto', sans-serif;
    font-size: 1.1rem;
    border: none;
}

.texto1 {
    margin-right: 60px;
}

</style>