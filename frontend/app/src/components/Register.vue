<template>
    <div>
        <q-form>
            <q-input
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

            <q-btn label="REGISTRARSE" type="button" color="black" id="register" @click="register"/>
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
                const registerFecth = await fetch('http://localhost:5000/auth/logon', {
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
                        profile_pic_fname: ''
                    })
                });
            
                const register = await registerFecth.json()
                
                if (register.type == 'error') {
                    this.$q.notify({
                        type: 'negative',
                        message: register.message
                    })
                } else {
                    this.$q.notify({
                        type: 'positive',
                        message: register.message
                    })
                    
                    this.$router.push('/login')
                }
            } else {
                this.$q.notify({
                    type: 'warning',
                    message: 'La contraseña no coincide'
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
    }
</style>