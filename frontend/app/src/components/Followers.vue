<template>
    <div>
        <q-list v-if="followers.length > 0">
            <q-item v-for="follower in followers" :key="follower.user_id">
                <q-item-section avatar>
                    <q-avatar v-if="follower.picture === '1' || follower.picture === ''">
                        <q-icon name='person' />
                    </q-avatar>
                    <q-avatar v-else size="30px" class="avatar">
                        <q-img
                            :src="follower.picture" class="bg-white" alt="foto_de_perfil"
                            style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                                border-radius:50%; border: 1px solid grey; margin: 5%;"
                            contain
                        />
                    </q-avatar>
                </q-item-section>
                <q-item-section>{{follower.username}}</q-item-section>
                <q-item-section>
                    <router-link :to="'/inside/user/'+follower.username" style="text-decoration: none;">
                        <q-btn label="VER PERFIL" color="black" style="width:100%;"/>
                    </router-link>
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
            followers: []
        }
    },
    async created() {
        const followersFetch = await this.$axios.get('https://localhost:5000/my/getFollowers', 
        {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const followers = followersFetch.data;

        followers.forEach(async a => {
            if (a.picture !== '1' && a.picture !== '') {
                a.picture = a.picture.replace("b'", 'data:image/png;base64,');
                a.picture = a.picture.replace("'", '');
            }
        })

        this.followers = followers;
    },
}
</script>

<style scoped>
</style>