<template>
    <q-layout view="hHh lpR fFf" id="admin-layout">
        <q-breadcrumbs>
            <q-breadcrumbs-el icon="home" to="/admin" />
            <q-breadcrumbs-el label="Usuario" icon="person" to="/start/pick-quasar-flavour" />
            <q-breadcrumbs-el label="Post" icon="photo_camera" to="/vue-components/breadcrumbs" />
        </q-breadcrumbs>
        <q-page-container id="user-list">
            <router-view />
        </q-page-container>
    </q-layout>
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

    #admin-layout {
        height: 100%;
        width: 70%;
        margin: 0 auto;
        padding: 1%;
    }

    #user-list::-webkit-scrollbar {
        display: none;
    }
    

    #user-list {
        padding: 1%;
        margin-top: 2%;
        max-height: 80vh;
        overflow-y: scroll;
    }


</style>