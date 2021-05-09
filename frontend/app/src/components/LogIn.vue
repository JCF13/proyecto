<template>
    <div>
        <q-form>
            <q-input
                filled
                label="Nombre de usuario"
                color="black"
                v-model="user.username"
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="person"/>
                </template>
            </q-input>
            
            <q-input
                filled
                label="Contraseña"
                type="password"
                color="black"
                v-model="user.password"
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="vpn_key"/>
                </template>
            </q-input>

            <q-btn type="button" id="google">
                <p>ENTRAR CON GOOGLE</p>
                <img src="./../assets/google.svg" alt="">
            </q-btn>

            <router-link to="/inside/home">
                <q-btn label="ENTRAR" type="button" color="black" id="entrar" @click="logIn"/>
            </router-link>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        async logIn() {
            
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

    #google {
        width: 50%;
        border-bottom-left-radius: 10px;
        font-weight: bold;        
    }

    #google p {
        padding-right: 5%;
    }

    #entrar {
        width: 50%;
        margin: 0 auto;
        border-bottom-right-radius: 10px;
        font-weight: bold;
    }

    a {
        text-decoration: none;
    }
</style>