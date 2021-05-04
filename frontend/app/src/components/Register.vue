<template>
    <div>
        <q-form>
            <q-input
                filled
                label="Nombre"
                color="black"
                v-model="user.name"
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
        async register() {
            
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