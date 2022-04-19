<template>
    <div class="container">
        <!-- Maximum call stack size exceeded (template dentro de template talvez), ver se existe alguma função recursiva
             Impedindo o card de funcionar corretamente. Maximum call stack size exceeded é excesso de chamada de função -->
             
        <Card>
            <template #header>
                <img alt="user header" src="demo/images/usercard.png">
            </template>
            <template #title>
                Advanced Card
            </template>
            <template #content>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
                quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!
            </template>
            <template #footer>
                <Button icon="pi pi-check" label="Save" />
                <Button icon="pi pi-times" label="Cancel" class="p-button-secondary" style="margin-left: .5em" />
            </template>
        </Card>
    </div>
</template>

<script>
import Card from 'primevue/card';

export default {
    components: {
        Card,    
    }
}
</script>

<style>

</style>