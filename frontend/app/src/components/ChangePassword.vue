<template>
    <div id="change-password-main">
        <h4>Cambiar contraseña</h4>
        <q-form id="form-password">
            <q-input
                type="password"
                label="Contraseña actual"
            />

            <q-input
                type="password"
                label="Nueva contraseña"
            />

            <q-input
                type="password"
                label="Repite la contraseña"
            />

            <q-btn label="GUARDAR" type="submit" color="black"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {

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
    #change-password-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-password {
        height: 70%;
        width: 90%;
        display: grid;
    }

    #form-password button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }
</style>