<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="top">
                <div id="left-top">
                    <q-img v-if="user.picture !== '1'"
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
                                    <q-btn flat color="black" icon="chat_bubble_outline" />
                                    <router-link to="/inside/settings">
                                        <q-btn flat round color="black" icon="settings" />
                                    </router-link>
                                </q-card-actions>
                            </q-card-section>
                            <q-card-section class="d-flex justify-between" horizontal>
                                <router-link to="/inside/social/followers">
                                    <q-btn class="bg-white" push :label="user.followers+' SEGUIDORES'" />
                                </router-link>
                                <router-link to="/inside/social/following">
                                    <q-btn class="bg-white" push :label="user.following+' SEGUIDOS'" />
                                </router-link>
                            </q-card-section>
                            <q-card-section class="d-flex justify-between" horizontal style="margin-top:5%">
                                <q-btn class="bg-white" push label="SEGUIR" @click="follow" />
                                <q-btn class="bg-white" push label="DEJAR DE SEGUIR" style="display:none" />
                                <q-btn class="bg-white" push label="TE SIGUE" />
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
        </div>
        <router-view/>
    </q-page>
</template>

<script>
export default {
    data() {
        return {
            user: {
                user_id: 0,
                username: '',
                picture: '',
                followers: 2,
                following: 4,
                posts: [
                    {
                        post_id: 0,
                        picture: '',
                        caption: '',
                    },
                ],
            },            
        }
    },
    async created() {
        if (this.$route.params.username) {
            const profileFetch = await fetch(`http://localhost:5000/my/getUser/${this.$route.params.username}`)
            const profile = await profileFetch.json();
            
            profile.posts.forEach(async post => {
                const imgFetch = await fetch('http://localhost:5000/my/image', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(post.picture)
                })
                
                const img = await imgFetch.json()

                img.picture = img.picture.replace("b'", 'data:image/png;base64,');
                img.picture = img.picture.replace("'", '');
                post.picture = img.picture;
            })

            const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(profile.picture)
            })

            const profilePic = await profilePicFetch.json();
            profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
            profilePic.picture = profilePic.picture.replace("'", '');
            profile.picture = profilePic.picture;
            
            this.user = profile;
        } else {
            const profileFetch = await fetch(`http://localhost:5000/my/getProfile`, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            })
            const profile = await profileFetch.json();
            
            profile.posts.forEach(async post => {
                const imgFetch = await fetch('http://localhost:5000/my/image', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(post.picture)
                });
                
                const img = await imgFetch.json();

                img.picture = img.picture.replace("b'", 'data:image/png;base64,');
                img.picture = img.picture.replace("'", '');
                post.picture = img.picture;
            });

            const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(profile.picture)
            })

            const profilePic = await profilePicFetch.json();
            profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
            profilePic.picture = profilePic.picture.replace("'", '');
            profile.picture = profilePic.picture;
            
            this.user = profile;
        }
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/profile/post/${id}`)
        },
        async follow() {
            const follow = await fetch('http://localhost:5000/my/foll', {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    user: {
                        id: 2,
                        username: 'prueba1',
                        profilePic: ''
                    },
                    follows: false
                })
            })
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
