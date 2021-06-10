<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="top">
                <div id="left-top">
                    <q-img v-if="user.picture !== '1' && user.picture !== ''"
                        :src="user.picture"
                        style="width:100%; max-width: 200px; height:100%; max-height: 175px; border-radius:50%; border: 2px solid black;"
                        contain
                    />
                    <q-icon v-else name='person' style="font-size: 150px; width:100%; max-width: 200px; height:100%; max-height: 175px; 
                        border-radius:50%; border: 2px solid black;" />
                </div>
                <div id="right-top">
                    <q-card class="my-card" flat>
                        <q-card-section vertical>
                            <q-card-section horizontal class="d-flex justify-between">
                                <h5><strong>{{user.username}}</strong></h5>

                                <q-card-actions horizontal class="q-px-md">
                                    <q-btn v-if="!isUser" flat color="black" icon="chat_bubble_outline" @click="createChat" />
                                    
                                    <router-link to="/inside/settings">
                                        <q-btn flat round color="black" icon="settings" />
                                    </router-link>
                                </q-card-actions>
                            </q-card-section>
                            <q-card-section class="d-flex justify-between" horizontal>
                                <router-link v-if="isUser" to="/inside/social/followers">
                                    <q-btn class="bg-white" push :label="user.followers+' SEGUIDORES'" />
                                </router-link>
                                <q-btn v-else class="bg-white" push :label="user.followers+' SEGUIDORES'" />
                                <router-link v-if="isUser" to="/inside/social/following">
                                    <q-btn class="bg-white" push :label="user.following+' SEGUIDOS'" />
                                </router-link>
                                <q-btn v-else class="bg-white" push :label="user.following+' SEGUIDOS'" />
                            </q-card-section>
                            <q-card-section class="d-flex justify-between" horizontal style="margin-top:5%">
                                <q-btn v-if="!isUser && !user.followed" class="bg-positive text-white" push label="SEGUIR" @click="follow" />
                                <q-btn v-if="!isUser && user.followed" class="bg-positive text-white" push label="SEGUIDO"/>
                                
                                <q-btn v-if="!isUser && user.followed" class="bg-negative text-white" push label="DEJAR DE SEGUIR" @click="unfollow" />
                                <q-btn v-if="!isUser && user.followYou" class="bg-positive text-white" push label="TE SIGUE" />
                            </q-card-section>
                        </q-card-section>
                    </q-card>
                </div>
            </div>

            <div v-if="user.posts.length > 0" id="publicaciones">
                <div v-for="post in user.posts" :key="post.post_id" @click="openPost(post.post_id)">
                    <img class="img-post" :src="post.picture" alt="" >
                </div>

                <div id="more">
                    <q-icon v-if="user.posts.length>5" name="add_circle_outline" size="30px"/>
                </div>
            </div>
            <div v-else>
                <h5 style="margin-left: 5%; margin-top: 5%;">Todavía no hay publicaciones</h5>
            </div>
        </div>
        <router-view/>
    </q-page>
</template>

<script>
export default {
    data() {
        return {
            user: {
                id: 0,
                username: '',
                picture: '',
                followers: 0,
                following: 0,
                posts: [
                    {
                        post_id: 0,
                        picture: '',
                        caption: '',
                    },
                ],
                followed: false,
                followYou: false
            },
            isUser: true,
        }
    },
    async created() {
        if (this.$route.params.username) {
            const profileFetch = await fetch(`https://localhost:5000/my/getUser/${this.$route.params.username}`, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            })
            
            const profile = await profileFetch.json();

            profile.posts.forEach(a => {
                a.picture = a.picture.replace("b'", 'data:image/png;base64,');
                a.picture = a.picture.replace("'", '');
            });
            
            profile.picture = profile.picture.replace("b'", 'data:image/png;base64,')
            profile.picture = profile.picture.replace("'", '');

            this.isUser = false;
            this.user = profile;
        } else {
            const profileFetch = await fetch(`https://localhost:5000/my/getProfile`, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            })
            const profile = await profileFetch.json();

            profile.posts.forEach(a => {
                a.picture = a.picture.replace("b'", 'data:image/png;base64,');
                a.picture = a.picture.replace("'", '');
            });
            
            profile.picture = profile.picture.replace("b'", 'data:image/png;base64,')
            profile.picture = profile.picture.replace("'", '');
            
            this.user = profile;
        }
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/profile/post/${id}`)
        },

        async unfollow() {
            const unfollowFetch = await fetch('https://localhost:5000/my/unfoll', {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    user: this.user.id
                })
            });

            const unfollow = await unfollowFetch.json();

            if (unfollow.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: unfollow.error_desc,
                    position: 'top-right'
                })

                this.user.followers--;
                this.user.followed = false;
            }
        },

        async follow() {
            const followFetch = await fetch('https://localhost:5000/my/foll', {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    user: this.user.id
                })
            })

            const follow = await followFetch.json()

            if (follow.error_type === 'negative') {
                this.$q.notify({
                    type: 'negative',
                    message: follow.error_desc,
                    position: 'top-right'
                });
            }

            if (follow.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: follow.error_desc,
                    position: 'top-right'
                });
                this.user.followers++;
                this.user.followed = true
            }
        },
        async createChat() {
            const chatFetch = await fetch('https://localhost:5000/chat/create', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                body: JSON.stringify({
                    partner_id: this.user.id
                })
            });

            const chat = await chatFetch.json();

            if (chat.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: chat.error_desc,
                    position: 'top-right'
                });

                this.$router.push(`/inside/chats/${chat.partner_id}`)
            }

            if (chat.error_type === 'warning') {
                this.$router.push(`/inside/chats/${chat.partner_id}`)
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

    #main {
        background: white;
        height: 90vh;
        width: 60%;
        box-shadow: 0 0 10px rgb(214, 214, 214);
        display: grid;
        grid-template-rows: 30% 70%;
        border-radius: 5px;
    }
    
    a {
        text-decoration: none;
        color: black;
    }

    #top {
        display: grid;
        width: 90%;
        height: 100%;
        margin: 0 auto;
        padding: 1%;
        grid-template-columns: 30% 70%;
        justify-content: space-between;
    }

    #left-top {
        background: whitesmoke;
        border-radius: 50%;
        max-width: 200px;
        max-height: 175px;
    }

    #publicaciones::-webkit-scrollbar {
        display: none;
    }

    #publicaciones {
        overflow-y: scroll;
        display: grid;
        grid-template-columns: 33.33% 33.33% 33.33%;
        grid-auto-rows: 60%;
        padding: 0 2%;
        margin: 2%;
    }

    #publicaciones div img {
        border: 1px solid whitesmoke;
    }

    .img-post {
        float: left;
        width: 100%;
        height: 100%;
        object-fit: contain;
        background: white;
    }

    #more {
        justify-self: center;
        align-self: center;
    }

</style>
