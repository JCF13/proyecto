<template>
    <div>
        <q-list v-if="following.length > 0">
            <q-item v-for="followed in following" :key="followed.user_id">
                <q-item-section avatar>
                    <q-avatar v-if="followed.picture === '1'">
                        <q-icon name='person' />
                    </q-avatar>
                    <q-avatar v-else size="30px" class="avatar">
                        <img :src="followed.picture" alt="">
                    </q-avatar>
                </q-item-section>
                <q-item-section>{{followed.username}}</q-item-section>
                <q-item-section>
                    <router-link :to="'/inside/user/'+followed.username" style="text-decoration: none;">
                        <q-btn label="VER PERFIL" color="black" style="width:100%;"/>
                    </router-link>
                </q-item-section>
                <q-item-section>
                    <q-btn label="DEJAR DE SEGUIR" color="black" @click="unfollow(followed.user_id)" />
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
            following: null
        }
    },
    async created() {
        const id = this.$route.params.id;

        const followingFetch = await fetch(`http://localhost:5000/my/getFollowing`, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const following = await followingFetch.json();

        following.forEach(async a => {
            if (a.picture !== '1') {
                const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(a.picture)
                })

                const profilePic = await profilePicFetch.json();
                profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
                profilePic.picture = profilePic.picture.replace("'", '');
                a.picture = profilePic.picture;
            }
        })

        this.following = following;
    },
    methods: {
        async unfollow(id) {
            const unfollowFetch = await fetch('http://localhost:5000/my/unfoll', {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    user: id
                })
            });

            const unfollow = await unfollowFetch.json();

            if (unfollow.type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: unfollow.message,
                    position: 'top-right'
                });

                this.following = this.following.filter(a => a.user_id != id)
            }


        },
    }
}
</script>

<style scoped>
</style>