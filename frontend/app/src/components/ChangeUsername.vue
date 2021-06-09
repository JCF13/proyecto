<template>
    <div id="change-username-main">
        <h4>Cambiar nombre de usuario</h4>
        <q-form id="form-username">
            <q-input
                label="Nombre de usuario"
                readonly
                :value="user.username"
            />

            <q-input
                label="Nuevo nombre de usuario"
                v-model="newUsername"
            />

            <q-btn label="GUARDAR" type="button" color="black" @click="updateUsername"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                user_id: 0,
                username: '',
                picture: ''
            },
            newUsername: ''
        }
    },
    async created() {
        const profileFetch = await fetch('https://localhost:5000/my/getProfile', {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        })

        const profile = await profileFetch.json();
        this.user = profile;
    },
    methods: {
        async updateUsername() {
            const usernameFetch = await fetch('https://localhost:5000/my/changeUsername', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                body: JSON.stringify({
                    username: this.newUsername
                })
            });

            const resp = await usernameFetch.json();

            if (resp.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: resp.error_desc,
                    position: 'top-right'
                });

                this.$router.push('/inside/profile')
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
    #change-username-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-username {
        height: 50%;
        width: 90%;
        display: grid;
    }

    #form-username button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }
</style>