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

            <q-btn label="ENTRAR" type="button" color="black" id="entrar" @click="logIn"/>
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
            const logInFetch = await fetch('http://localhost:5000/auth/login', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.user.username,
                    passwd: this.user.password
                })
            });

            if (logInFetch.status === 200) {
                const token = await logInFetch.json();
    
                localStorage.setItem('access_token', token.your_auth.access_token);
                localStorage.setItem('refresh_token', token.your_auth.refresh_token);

                this.$router.push('/inside')
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