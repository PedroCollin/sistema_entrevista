<div class="stepsdemo-content">
    <Card>
        <template #title>
            Personal Information
        </template>
        <template #subtitle>
            Enter your information
        </template>
        <template #content>
            <p class="p-text-secondary">Enter your information</p>
            <div class="p-fluid">
                <div class="field">
                    <label for="firstname">Firstname</label>
                    <InputText id="firstname" v-model="$v.firstname.$model" :class="{'p-invalid':$v.firstname.$invalid && submitted}" />
                    <small v-show="$v.firstname.$invalid && submitted" class="p-error">Firstname is required.</small>
                </div>
                <div class="field">
                    <label for="lastname">Lastname</label>
                    <InputText v-model="$v.lastname.$model" :class="{'p-invalid':$v.lastname.$invalid && submitted}" />
                    <small v-show="$v.lastname.$invalid && submitted" class="p-error">Lastname is required.</small>
                </div>
                <div class="field">
                    <label for="age">Age</label>
                    <InputText id="age" v-model="$v.age.$model" :class="{'p-invalid':$v.age.$error && submitted}" />
                    <small v-show="$v.age.$invalid && submitted" class="p-error">Age should be a number.</small>
                </div>
            </div>
        </template>
        <template #footer>
            <div class="grid grid-nogutter justify-content-between">
                <i></i>
                <Button label="Next" @click="nextPage(!$v.$invalid)" icon="pi pi-angle-right" iconPos="right" />
            </div>
        </template>
    </Card>
</div>