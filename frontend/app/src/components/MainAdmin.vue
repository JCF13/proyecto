<template>
    <q-list>
        <q-item v-for="user in users" :key="user.id">
            <q-item-section avatar>
                <q-avatar v-if="user.picture === '1' || user.picture === ''">
                    <q-icon name='person' />
                </q-avatar>
                <q-avatar v-else>
                    <q-img
                        :src="user.picture" class="bg-white"
                        style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                            border-radius:50%; border: 1px solid grey; margin: 5%;"
                        contain
                    />
                </q-avatar>
            </q-item-section>
            <q-item-section>{{user.username}}</q-item-section>
            <q-item-section>
                <q-btn label="ELIMINAR" color="black" @click="deleteUser(user.id)" />
            </q-item-section>
        </q-item>
    </q-list>
</template>

<script>
export default {
    data() {
        return {
            users: []
        }
    },
    async created() {
        const usersFetch = await this.$axios.get('https://localhost:5000/admin/getAll',
        {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const users = usersFetch.data;

        users.forEach(async a => {
            if (a.picture !== '' && a.picture !== '1') {
                a.picture = a.picture.replace("b'", 'data:image/png;base64,');
                a.picture = a.picture.replace("'", '');
            }
        });

        this.users = users;
    },
    methods: {
        async deleteUser(id) {
            const deleteFetch = await this.$axios.post('https://localhost:5000/admin/delete',
            {
                user_id: id
            },
            {
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            });

            const resp = deleteFetch.data;

            if (resp.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: resp.error_desc,
                    position: 'top-right'
                });
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

</style>