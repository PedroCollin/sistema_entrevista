<template>
    <div>
        <div>
            <Carousel :value="imgs" :numVisible="4" :numScroll="3" :responsiveOptions="responsiveOptions">
                <template #item="slotProps">
                    <div class="car-item">
                        <div class="car-content">
                            <div>
                                <img class="carousel-style" :src="slotProps.data.src"/>
                            </div>
                        </div>
                    </div>
                </template>
            </Carousel>
        </div>
        <div>
            <TabView>
                <TabPanel header="Passo a Passo">
                    <div class="card">
                        <h5>Right Align</h5>
                        <Timeline :value="events1" align="right">
                            <template #content="slotProps">
                                {{slotProps.item.status}}
                            </template>
                        </Timeline>
                    </div>
                </TabPanel>
                <TabPanel header="Perguntas Frequentes">
                    <Accordion>
                        <AccordionTab header="Testes">
                            Content
                        </AccordionTab>
                        <AccordionTab header="Header II">
                            Content
                        </AccordionTab>
                        <AccordionTab header="Header III">
                            Content
                        </AccordionTab>
                    </Accordion>
                </TabPanel>
                <TabPanel header="Header III">
                    Content III
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
                {status: 'Ordered', date: '15/10/2020 10:30', icon: 'pi pi-shopping-cart', color: '#9C27B0', image: 'game-controller.jpg'},
                {status: 'Processing', date: '15/10/2020 14:00', icon: 'pi pi-cog', color: '#673AB7'},
                {status: 'Shipped', date: '15/10/2020 16:15', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Delivered', date: '16/10/2020 10:00', icon: 'pi pi-check', color: '#607D8B'}
            ],
            imgs:[
                {
                    src:"teste1.jpg",
                },
                {
                    src:"homoge.jpg",
                }
            ]
	    }
    }
}
</script>

<style lang="scss" scoped>
.carousel-style{
    height: 60vh;
    width: 200vh;
}
</style>