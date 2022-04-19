<template>
    <div class="container">
        <template class="header">
            <img alt="user header" src="demo/images/usercard.png">
        </template>
        <template class="title">
            Advanced Card
        </template>
        <template class="content">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
            quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!
        </template>
        <template class="footer">
            <Button icon="pi pi-check" label="Save" />
            <Button icon="pi pi-times" label="Cancel" class="p-button-secondary" style="margin-left: .5em" />
        </template>
    </div>
</template>

<script>
import Card from 'primevue/card';

export default {
    name: "Card",
}
</script>

<style>

</style>