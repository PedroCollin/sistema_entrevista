<template>
    <!-- Colocar links de politica de privacidade, contato e FAQ -->
    <center>
        <div class="container">
            <div class="footer">
                <div class="colunaEsquerda">
                    Tecnologia para a Vida
                    <div class="innerText">
                        © Robert Bosch Ltda. 2022, todos os direitos reservados
                    </div>
                </div>
                <div class="colunaDireita">
                    <a class="opcao1" href="" style="text-decoration: none; color: inherit">Política de Privacidade</a>
                    <h3 class="separador"> - </h3>
                    <a class="opcao2" href="" style="text-decoration: none; color: inherit">Entre em Contato</a>
                </div>
            </div>
        </div>
    </center>
</template>

<script>
export default {
    name: 'Footer',
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

@media only screen and (max-width: 1000px) {
    .footer {
        margin-top: auto;
        height: auto;
        bottom: 0;
        border-top: 1px solid rgb(238, 238, 238);
        padding: 10px 10px 10px 10px;
        width: 100%;
        background-color: rgb(255, 255, 255);
        font-family: 'Roboto', sans-serif;
        font-size: 10px;
    }

    .colunaEsquerda {
        width: 50%;
    }

    .colunaEsquerda > .innerText {
        margin-top: 1.5vh;
        margin-bottom: 2.5vh;
    }

    .colunaDireita {
        display:flex;
        flex-direction: column;
    }

    .opcao1 {
        margin-top: 2vh;
    }

    /* .opcao2 {
        width: 100%;
    } */
}

@media screen and (min-width: 1000px){
    .footer {
        margin-top: auto;
        height: auto;
        bottom: 0;
        display: flex;
        border-top: 1px solid rgb(241, 241, 241);
        padding: 10px 10px 10px 10px;
        width: 100%;
        background-color: rgb(255, 255, 255);
        font-family: 'Roboto', sans-serif;
        text-align: left;
        font-size: 16px;
    }

    .colunaEsquerda {
        width: 50%;
    }

    .colunaEsquerda > .innerText {
        margin-top: 2vh;
    }

    .colunaDireita {
        width: 50%;
        border-left: 20px;
        border-right: 20px;
        text-align: center;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }

    .opcao1 {
        margin-left: 24rem;
        margin-right: 2rem;
    }

    .opcao2 {
        margin-right: 2rem;
        margin-left: 2rem;
    }

    .separador {
        display: none;
    }
}

* {
    padding: 0;
    margin: 0;
    border: 0;
    box-sizing: border-box;
}

</style>