<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="left">
                <q-list id="settings-list">
                    <router-link to="/inside/settings/change-username">
                        <q-item clickable v-ripple>
                            <q-item-section avatar>
                                <q-icon color="black" name="person" />
                            </q-item-section>

                            <q-item-section>Nombre de usuario</q-item-section>
                        </q-item>
                    </router-link>

                    <q-separator />
                    
                    <router-link to="/inside/settings/change-password">
                        <q-item clickable v-ripple>
                            <q-item-section avatar>
                                <q-icon color="black" name="security" />
                            </q-item-section>

                            <q-item-section>Contraseña</q-item-section>
                        </q-item>
                    </router-link>

                    <q-separator />
                    
                    <router-link to="/inside/settings/change-profilepic">
                        <q-item clickable v-ripple>
                            <q-item-section avatar>
                                <q-icon color="black" name="camera" />
                            </q-item-section>
                            <q-item-section>Foto de perfil</q-item-section>
                        </q-item>
                    </router-link>

                    <q-separator />
                    
                    <router-link to="/inside/settings/account-information">
                        <q-item clickable v-ripple>
                            <q-item-section avatar>
                            <q-icon color="black" name="manage_accounts" />
                            </q-item-section>

                            <q-item-section>Información</q-item-section>
                        </q-item>
                    </router-link>
                    
                    <q-separator />
                </q-list>
            </div>
            <div id="right">
                <router-view/>
            </div>
        </div>
    </q-page>
</template>

<script>
export default {
    data() {
        return {
        }
    },
}
</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #main {
        background: white;
        height: 80vh;
        width: 60%;
        box-shadow: 0 0 10px rgb(214, 214, 214);
        display: grid;
        grid-template-columns: 25% 75%;
    }
    
    a {
        text-decoration: none;
        color: black;
    }

    #right {
        margin: 0 auto;
        width: 90%;
        height: 100%;
    }

    #settings-list {
        height: 100%;
        border-right: 1px solid black;
    }

    #settings-list div {
        padding-left: 2%;
    }

    hr {
        background: black;
    }
</style>
