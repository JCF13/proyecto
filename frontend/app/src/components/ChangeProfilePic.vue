<template>
    <div id="change-profilepic-main">
        <h4>Cambiar foto de perfil</h4>
        <q-form id="form-profilepic">
            <q-file clearable filled v-model="model" label="Nueva foto de perfil" />

            <div id="new-pic">
                Foto
            </div>

            <q-btn label="GUARDAR" type="submit" color="black"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            model: null
        }
    }
}
</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    #change-profilepic-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-profilepic {
        height: 70%;
        width: 90%;
        display: grid;
    }

    #form-profilepic button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }

    #new-pic {
        height: 100%;
    }
</style>