<template>
    <div>
        <q-form>
            <q-input 
                class="bg-white"
                filled
                label="Nombre"
                color="black"
                v-model="user.name"
                :rules="[
                    val => val.length > 2
                ]"
                lazy-rules
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="badge"/>
                </template>
            </q-input>

            <q-input 
                class="bg-white"
                filled
                label="Apellidos"
                color="black"
                v-model="user.surnames"
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="badge"/>
                </template>
            </q-input>

            <q-input 
                class="bg-white"
                filled
                label="Correo electrónico"
                color="black"
                type="email"
                v-model="user.email"
                :rules="[ validEmail ]"
                lazy-rules
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="mail"/>
                </template>
            </q-input>

            <q-input 
                class="bg-white"
                filled
                label="Nombre de usuario"
                color="black"
                v-model="user.username"
                :rules="[val => val.length >= 4]"
                lazy-rules
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

            <q-input 
                class="bg-white"
                filled
                label="Repetir contraseña"
                type="password"
                color="black"
                v-model="user.confirmPassword"
                :rules="[val => val == this.user.password]"
                lazy-rules
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="vpn_key"/>
                </template>
            </q-input>

            <q-btn label="REGISTRARSE" type="button" id="register" @click="register"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                name: '',
                surnames: '',
                email: '',
                username: '',
                password: '',
                confirmPassword: ''
            }
        }
    },
    methods: {
        validEmail() {
            const pattern = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
            return pattern.test(this.user.email);
        },
        async register() {
            if (this.user.password == this.user.confirmPassword) {
                const registerFecth = await fetch('https://localhost:5000/auth/logon', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.user.username,
                        name: this.user.name,
                        surname: this.user.surnames,
                        password: this.user.password,
                        email: this.user.email,
                        picture: ''
                    })
                });
            
                const register = await registerFecth.json()
                
                if (register.type == 'error') {
                    this.$q.notify({
                        type: 'negative',
                        message: register.message,
                        position: 'top-right'
                    })
                } else {
                    this.$q.notify({
                        type: 'positive',
                        message: register.message,
                        position: 'top-right'
                    })
                    
                    this.$router.push('/login')
                }
            } else {
                this.$q.notify({
                    type: 'warning',
                    message: 'La contraseña no coincide',
                    position: 'top-right'
                })
            }
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

    #register {
        width: 100%;
        margin: 0 auto;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
        font-weight: bold;
    }
</style>