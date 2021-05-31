<template>
    <q-layout view="hHh lpR fFf" id="access-layout">
        <div id="menu-access">
            <q-toolbar class="row d-flex justify-content-center" id="option-access">
                <q-tabs class="col-md-12">
                    <router-link to="/login" class="col-md-6">
                        <q-tab name="tab1" label="ENTRAR" />
                    </router-link>
            
                    <router-link to="/register" class="col-md-6">
                        <q-tab name="tab2" label="REGISTRARSE" />
                    </router-link>
                </q-tabs>
            </q-toolbar>
            
            <q-page-container>
                <router-view />
            </q-page-container>
        </div>
  </q-layout>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Nunito', sans-serif;
    }

    #access-layout {
        height: 100%;
        width: 70%;
        margin: 0 auto;
        padding: 5%;
        background: #b3e5fc;
    }

    a {
        text-decoration: none;
        color: black;
    }

    #menu-access {
        background: linear-gradient(to left, #4fc3f7, #b2ff59);
        box-shadow: 0 0 10px rgb(161, 161, 161);
        border-radius: 10px;
    }


</style>