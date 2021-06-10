<template>
    <div>
        <q-form>
            <q-input 
                class="bg-white"
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
                class="bg-white"
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

            <q-btn label="ENTRAR" type="button" id="entrar" @click="logIn"/>
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
    created() {
        window.gapi.load('auth2', () => {
            const auth2 = window.gapi.auth2.init({
                client_id: '969437755795-mas4cecbtrqrd38pa9hodgbjtkssoeqs.apps.googleusercontent.com'
            });
            auth2.attachClickHandler(document.querySelector('#google'), {}, async (googleUser) => {
                console.log(googleUser);
                const id_token = googleUser.qc.id_token;

                console.log(id_token);
            });
        });
    },
    methods: {
        async logIn() {
            const logInFetch = await this.$axios.post('https://localhost:5000/auth/login', 
            {
                username: this.user.username,
                passwd: this.user.password
            }, 
            {
                headers: {
                    'Content-type': 'application/json'
                }
            })
            
            const login = logInFetch.data;

            if (!login.error.error_type) {
                localStorage.setItem('access_token', login.your_auth.access_token);
                localStorage.setItem('refresh_token', login.your_auth.refresh_token);

                if (login.your_auth.role === 'admin') {
                    localStorage.setItem('role', 'admin');
                    this.$router.push('/admin');
                } else this.$router.push('/inside')
            } else {
                this.$q.notify({
                    type: 'negative',
                    message: login.error.error_desc,
                    position: 'top'
                });
            }

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