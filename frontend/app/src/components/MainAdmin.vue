<template>
    <q-list>
        <q-item v-for="user in users">
            <q-item-section avatar>
                <q-avatar>
                    <img src="https://cdn.quasar.dev/img/boy-avatar.png">
                </q-avatar>
            </q-item-section>
            <q-item-section>Usuario1</q-item-section>
            <q-item-section>
                <q-btn label="ADMINISTRAR USUARIO" color="black"/>
            </q-item-section>
            <q-item-section>
                <q-btn label="ELIMINAR" color="black" />
            </q-item-section>
        </q-item>
    </q-list>
</template>

<script>
export default {
    data() {
        return {
            users: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
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

</style>