<template>
    <q-layout view="hHh lpR fFf" id="social-layout">
        <div id="menu-access">
            <q-toolbar class="row d-flex justify-content-center">
                <q-tabs class="col-md-12">
                    <router-link to="/inside/social/followers" class="col-md-6" role="tab">
                        <q-tab name="tab1" label="SEGUIDORES" />
                    </router-link>
            
                    <router-link to="/inside/social/following" class="col-md-6" role="tab">
                        <q-tab name="tab2" label="SEGUIDOS" />
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

    #menu-access {
        background: white;
        box-shadow: 0 0 10px rgb(161, 161, 161);
        border-radius: 10px;
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
    }
</style>