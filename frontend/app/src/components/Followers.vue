<template>
    <div>
        <q-list v-if="followers.length > 0">
            <q-item v-for="follower in followers" :key="follower.user_id">
                <q-item-section avatar>
                    <q-avatar v-if="follower.picture === '1' || follower.picture === ''">
                        <q-icon name='person' />
                    </q-avatar>
                    <q-avatar v-else size="30px" class="avatar">
                        <img :src="follower.picture" alt="">
                    </q-avatar>
                </q-item-section>
                <q-item-section>{{follower.username}}</q-item-section>
                <q-item-section>
                    <router-link :to="'/inside/user/'+follower.username" style="text-decoration: none;">
                        <q-btn label="VER PERFIL" color="black" style="width:100%;"/>
                    </router-link>
                </q-item-section>
                <q-item-section>
                    <q-btn label="ELIMINAR SEGUIDOR" color="black" @click="deleteFollower(follower.user_id)" />
                </q-item-section>
            </q-item>
        </q-list>
        <div v-else style="padding-left: 5%; padding-bottom: 1%;">
            <h6>Todavía no hay ningún seguidor</h6>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            followers: null
        }
    },
    async created() {
        const id = this.$route.params.id;

        const followersFetch = await fetch(`https://localhost:5000/my/getFollowers`, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const followers = await followersFetch.json();

        followers.forEach(async a => {
            if (a.picture !== '1' && a.picture !== '') {
                const profilePicFetch = await fetch('https://localhost:5000/my/image', {
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

        this.followers = followers;
    },
    methods: {
        async deleteFollower(follower_id) {

        }
    }
}
</script>

<style scoped>
</style>