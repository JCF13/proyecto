<template>
    <div>
        <q-list v-if="following.length > 0">
            <q-item v-for="followed in following" :key="followed.id">
                <q-item-section avatar>
                    <q-avatar v-if="followed.picture === '1' || followed.picture === ''">
                        <q-icon name='person' />
                    </q-avatar>
                    <q-avatar v-else size="30px" class="avatar">
                        <q-img
                            :src="followed.picture" class="bg-white" alt="foto_de_perfil"
                            style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                                border-radius:50%; border: 1px solid grey; margin: 5%;"
                            contain
                        />
                    </q-avatar>
                </q-item-section>
                <q-item-section>{{followed.username}}</q-item-section>
                <q-item-section>
                    <router-link :to="'/inside/user/'+followed.username" style="text-decoration: none;">
                        <q-btn label="VER PERFIL" color="black" style="width:100%;"/>
                    </router-link>
                </q-item-section>
                <q-item-section>
                    <q-btn label="DEJAR DE SEGUIR" color="black" @click="unfollow(followed.id)" />
                </q-item-section>
            </q-item>
        </q-list>
        <div style="padding-left: 5%; padding-bottom: 2%;" v-else>
            <h5>Todavía no sigues a ningún usuario</h5>
            <router-link to="/inside/search" style="text-decoration: none;">
                <q-btn label='Empezar a seguir usuarios' push color='black' />
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            following: []
        }
    },
    async created() {
        const followingFetch = await this.$axios.get('https://localhost:5000/my/getFollowing',
        {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const following = followingFetch.data;

        following.forEach(async a => {
            if (a.picture !== '1' && a.picture !== '') {
                a.picture = a.picture.replace("b'", 'data:image/png;base64,');
                a.picture = a.picture.replace("'", '');
            }
        })

        this.following = following;
    },
    methods: {
        async unfollow(id) {
            const unfollowFetch = await this.$axios.patch('https://localhost:5000/my/unfoll',
            {
                user: id
            },
            {
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            });

            const unfollow = unfollowFetch.data;

            if (unfollow.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: unfollow.error_desc,
                    position: 'top-right'
                });

                this.following = this.following.filter(a => a.id != id)
            }
        },
    }
}
</script>

<style scoped>
</style>