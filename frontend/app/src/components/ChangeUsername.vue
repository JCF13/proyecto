<template>
    <div id="change-username-main">
        <h4>Cambiar nombre de usuario</h4>
        <q-form id="form-username">
            <q-input
                label="Nombre de usuario"
                readonly
                :value="username"
            />

            <q-input
                label="Nuevo nombre de usuario"
                v-model="newUsername"
            />

            <q-btn label="GUARDAR" type="submit" color="black"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: 'Nombre_de_usuario',
            newUsername: null
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
    #change-username-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-username {
        height: 50%;
        width: 90%;
        display: grid;
    }

    #form-username button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }
</style>