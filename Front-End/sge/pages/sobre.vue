<template>
    <div>
        <div>
            <TabView>
                <TabPanel header="Guia de Utilização">
                    <div class="card">
                        <Timeline :value="events1">
                            <template #opposite="slotProps">
                                <small class="p-text-secondary">{{slotProps.item.desc}}</small>
                            </template>
                            <template #content="slotProps">
                                {{slotProps.item.status}}
                            </template>
                        </Timeline> 
                    </div>
                </TabPanel>
                <TabPanel header="Perguntas Frequentes">
                    <div class="accordion">
                        <Accordion>
                            <AccordionTab header="Como adiciono uma Dinâmica?">
                                No canto superior direito, há um botão azul que abrirá um Menu. Nele, é possível clicar em "Cadastrar Dinâmica". 
                                Na tela que abrirá, adicione as informações solicitadas e clique no botão verde "Registrar Dinâmica".
                            </AccordionTab>
                            <AccordionTab header="Como cadastro um novo Usuário?">
                                No canto superior direito, há um botão azul que abrirá um Menu. Nele, é possível clicar em "Cadastrar Usuário". 
                                Na tela que abrirá, adicione as informações solicitadas e clique no botão azul "Cadastrar".
                            </AccordionTab>
                            <AccordionTab header="Como posso adicionar uma turma nova?">
                                Na Página Inicial há um botão branco com um símbolo de +. Ao clicar nele, será possível adicionar uma nova turma,
                                adicionando as informações solicitadas e clicando no botão.
                            </AccordionTab>
                        </Accordion>
                    </div>
                </TabPanel>
            </TabView>
        </div>
    </div>   
</template>

<script>
export default {
    data() {
        return {
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
		    ],
            events1: [
                {status: 'Login', desc: 'Primeiro, faça login no sistema...', icon: 'pi pi-shopping-cart', color: '#9C27B0', image: 'game-controller.jpg'},
                {status: 'Home', desc: 'Aqui, é possível abrir novos cursos, turmas, ou ver informações sobre as existentes.', icon: 'pi pi-cog', color: '#673AB7'},
                {status: 'Cadastro de Cursos', desc: 'Na tela de Cadastro de Cursos, pode-se adicionar uma carga horária, o período que será realizado e mais...', icon: 'pi pi-check', color: '#607D8B'},
                {status: 'Cadastro de Dinâmicas', desc: 'Na tela de Cadastro de Dinâmicas, pode-se colocar um descrição, os critérios a serem avaliados e mais...', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Cadastro de Vagas', desc: 'Na aba de Cadastro de vagas, é possível adicionar a quantidade de vagas de um curso, data e mais...', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Entrevistas', desc: 'Na tela de Entrevistas, é possível selecionar um candidato, definir informações e pontuação nos critérios a serem avaliados na entrevista.', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Dinâmicas', desc: 'Na aba de Dinâmicas, pode-se selecionar um candidato, definir informações e pontuação nos critérios a serem avaliados na dinâmica.', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Sobre', desc: 'Aqui na tela "Sobre o Sistema", você pode tirar suas dúvidas gerais sobre o sistema e seu funcionamento!', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Contato', desc: 'Caso tenha ficado alguma dúvida, clique em "Entre em contato" e converse conosco!', icon: 'pi pi-shopping-cart', color: '#FF9800'},
            ],
	    }
    }
}
</script>

<style lang="scss" scoped>
.card{
    margin-bottom: 8.5vh;
    margin-top: 5vh;
    margin-left: 20vh;
}

.accordion{
    margin-bottom: 55.4vh;
    margin-top: 5vh;
}
</style>