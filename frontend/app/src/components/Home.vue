<template>
    <q-page class="flex flex-center" id="page">        
        <div id="main" class="flex flex-center">
            <q-card class="my-card" v-for="post in posts" :key="post.id">
                <q-item class="card-top">
                    <q-item-section avatar>
                        <q-avatar v-if="post.creator.picture == 1">
                            <q-icon name='person' />
                        </q-avatar>
                        <q-avatar v-else>
                            <img :src="post.creator.picture" />
                        </q-avatar>
                    </q-item-section>

                    <q-item-section>
                        <q-item-label><strong>{{post.creator.username}}</strong></q-item-label>
                        <q-item-label>{{post.caption}}</q-item-label>
                    </q-item-section>

                    <q-item-section align="right" class="info-post">
                        <q-item-label>
                            {{post.comments.length}} <q-icon name="comment" />
                        </q-item-label>
                        <q-item-label>
                            {{post.likes.length}} <q-icon name="favorite" color="red" @click="sendLike(post.id)" />
                        </q-item-label>
                    </q-item-section>
                </q-item>

                <q-icon class="liked" :data-post='post.post_id' @click="sendLike(post.post_id)" name='favorite_outline' color='red' style="position: absolute; right: 0; font-size: 40px;" />

                <img @click="openPost(post.post_id)" :src="post.picture" alt="">
            </q-card>
            <h5 v-if="posts.length === 0">Todavía no hay publicaciones para ver</h5>
            
            <div id="more" v-if="posts.lenght > 0">
                <q-icon name="add_circle_outline" size="30px" @click="loadMore" />
            </div>
        </div>
        <q-page-sticky position="bottom-right" :offset="[18, 18]">
            <q-btn fab icon="arrow_upward" color="blue" />
        </q-page-sticky>
        <router-view/>
    </q-page>
</template>

<script>
export default {
    data() {
        return {
            posts: [
                {
                    id: 0,
                    picture: '',
                    caption: '',
                    creationDate: '',
                    creator: {
                        user_id: 0,
                        username: '',
                        picture: ''
                    },
                    comments: [
                        {
                            id: 0,
                            user: {
                                id: 0,
                                username: ''
                            },
                            message: '',
                            creationDate: ''
                        }
                    ],
                    liked: false,
                    likes: [
                        {
                            id: 0,
                            user: {
                                id: 0,
                                username: ''
                            }
                        },
                    ]
                },
            ],
            page: 0,
            user: {
                id: null,
            }
        }
    },
    async created() {
        const postsFetch = await fetch(`http://localhost:5000/post/gposts/${this.page}`, {
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });
        const posts = await postsFetch.json();

        posts.forEach(async post => {
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

            if (post.creator.picture !== '1') {
                const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(post.creator.picture)
                })

                const profilePic = await profilePicFetch.json();
                profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
                profilePic.picture = profilePic.picture.replace("'", '');
                post.creator.picture = profilePic.picture;
            }
        })

        this.posts = posts;
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/home/post/${id}`)
        },

        async sendLike(id) {
            this.posts.filter(post => {
                if (post.post_id === id) {
                    document.querySelector(`i[data-post='${id}']`).innerHTML = 'favorite'
                }
            })
        },

        async loadMore() {
            this.page += 1;

            const postsFetch = await fetch(`http://localhost:5000/post/gposts/${this.page}`, {
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            });
            const posts = await postsFetch.json();

            posts.forEach(async post => {
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

                if (post.creator.picture !== '1') {
                    const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json'
                        },
                        body: JSON.stringify(post.creator.picture)
                    })

                    const profilePic = await profilePicFetch.json();
                    profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
                    profilePic.picture = profilePic.picture.replace("'", '');
                    post.creator.picture = profilePic.picture;
                }
                
                this.posts.push(post);
            })

            if (posts.length < 10) {
                document.querySelector('#more i').style.display = 'none'
            }
        },
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
        display: grid;
        width: 45%;
    }

    #main::-webkit-scrollbar {
        display: none;
    }

    .my-card img {
        max-width: 500px;
        max-height: 500px;
        object-fit: contain;
    }

    #more {
        justify-self: center;
        margin: 5% 0;
    }

    .my-card {
        margin-top: 5%;
    }

    .card-top {
        padding-left: 1%;
        background: linear-gradient(to left, #4fc3f7, #b2ff59);
        border-bottom: 1px solid rgb(128, 128, 128);
    }

    .info-post {
        padding-right: 1%;
    }

    a {
        text-decoration: none;
    }

    img {
        background: white;
    }

</style>