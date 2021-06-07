<template>
    <div id="change-password-main">
        <h4>Cambiar contraseña</h4>
        <q-form id="form-password">
            <q-input
                v-model="password"
                type="password"
                label="Contraseña actual"
            />

            <q-input
                v-model="newPassword"
                type="password"
                label="Nueva contraseña"
            />

            <q-input
                v-model="repeatPassword"
                type="password"
                label="Repite la contraseña"
            />

            <q-btn label="GUARDAR" type="button" color="black" @click="updatePassword"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            password: '',
            newPassword: '',
            repeatPassword: ''
        }
    },
    methods: {
        async updatePassword() {
            if (this.newPassword === this.repeatPassword) {
                const passwordFetch = await fetch('https://localhost:5000/my/changePassword', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json',
                        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                    },
                    body: JSON.stringify({
                        password: this.password,
                        new_password: this.newPassword
                    })
                });

                const resp = await passwordFetch.json();

                if (resp.type === 'positive') {
                    this.$q.notify({
                        type: 'positive',
                        message: resp.message,
                        position: 'top-right'
                    });

                    this.$router.push('/inside/profile')
                }

                if (resp.type === 'negative') {
                    this.$q.notify({
                        type: 'negative',
                        message: resp.message,
                        position: 'top-right'
                    })
                }

            } else {
                this.$q.notify({
                    type: 'warning',
                    message: 'La contraseña no coincide',
                    position: 'top'
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
    #change-password-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-password {
        height: 70%;
        width: 90%;
        display: grid;
    }

    #form-password button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }
</style>