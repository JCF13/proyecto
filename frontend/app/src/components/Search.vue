<template>
    <q-layout view="hHh lpR fFf" id="social-layout">
        <div id="menu-search">
            <q-toolbar class="row d-flex justify-content-center">
                <q-input color="grey-3" class="col-sm-12" v-model="text" label="Buscar usuario">
                    <template v-slot:append>
                        <q-icon name="person_search" color="black" />
                    </template>
                </q-input>
            </q-toolbar>
            <q-page-container>
                <router-view />
            </q-page-container>
        </div>
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
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #social-layout {
        height: 100%;
        width: 70%;
        margin: 0 auto;
        padding: 2%;
    }

    a {
        text-decoration: none;
        color: black;
    }

    #menu-search {
        background: white;
        box-shadow: 0 0 10px rgb(161, 161, 161);
        border-radius: 10px;
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
        padding: 1%;
    }
</style>