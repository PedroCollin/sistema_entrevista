<template>
    <div class="mainDiv">
        <header class="header"></header>
        <subheader class="subHeader">
            <img class="BoschLogo" src="../assets/images/BoschLogo.png" alt="Logo Bosch">
            <div class="subDiv">
                <img class="svgImage" src="../assets/images/bars-solid.svg" alt="Botão Hamburger" height="30px" width="30px" />
            </div>
        </subheader>
    </div>
</template>

<script>
export default {
    name: "Header"
    
};
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

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
    margin-bottom: 1.4rem;
    
}

@media only screen and (max-width: 1456px) {
    
}

.subDiv {
    left: 600px;
    top: 2rem;
    margin-right: 1rem;
    font-family: 'Roboto', sans-serif;
    font-size: 1.1rem;
    border: none;
    margin-left: auto; 
    margin-bottom: 0.5rem;
}

.mainDiv {
    background-color: #ffffff;
}

</style>