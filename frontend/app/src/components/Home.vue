<template>
    <q-page class="flex flex-center" id="page">        
        <div id="main" class="flex flex-center">
            <q-card class="my-card" v-for="post in posts" :key="post.id">
                <q-item class="card-top">
                    <q-item-section avatar>
                        <q-avatar v-if="post.creator.picture === '1' || post.creator.picture === ''">
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
                            {{post.likes.length}} <q-icon name="favorite" color="red" />
                        </q-item-label>
                    </q-item-section>
                </q-item>

                <q-icon v-if="!post.liked" @click="sendLike(post.post_id)" name='favorite_outline' color='red' style="position: absolute; left: 0; bottom: 0; font-size: 40px;" />
                <q-icon v-else name='favorite' @click="deleteLike(post.post_id)" color='red' style="position: absolute; left: 0; bottom: 0; font-size: 40px;" />

                <img @click="openPost(post.post_id)" :src="post.picture" alt="">
            </q-card>
            <div v-if="posts.length === 0" style="display: flex; flex-direction: column;">
                <h5>Todavía no hay publicaciones para ver</h5>
                <router-link to="/inside/search">
                    <q-btn style="width: 100%;" label='Buscar otros usuarios' color='black' />
                </router-link>
            </div>
            
            <div id="more" v-else>
                <q-icon name="add_circle_outline" size="30px" @click="loadMore" />
            </div>
        </div>
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
                                username: '',
                                picture: ''
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
                                username: '',
                                picture: ''
                            }
                        }
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
        const postsFetch = await fetch(`https://localhost:5000/post/gposts?page=${this.page}`, {
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                'page': this.page
            }
        });
        const posts = await postsFetch.json();

        posts.forEach(post => {
            post.picture = post.picture.replace("b'", 'data:image/png;base64,');
            post.picture = post.picture.replace("'", '');

            if (post.creator.picture !== '1' && post.creator.picture !== '') {
                post.creator.picture = post.creator.picture.replace("b'", 'data:image/png;base64,');
                post.creator.picture = post.creator.picture.replace("'", '');
            }
        })

        this.posts = posts;
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/home/post/${id}`)
        },
        
        async sendLike(id) {
            this.posts.filter(async post => {
                if (post.post_id === id) {
                    const likeFetch = await fetch('https://localhost:5000/my/like', {
                        method: 'PATCH',
                        headers: {
                            'Content-type': 'application/json',
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                        },
                        body: JSON.stringify({
                            post_id: id
                        })
                    });

                    const like = await likeFetch.json()

                    if (like.error_type === 'positive') {
                        this.$q.notify({
                            type: 'positive',
                            message: like.error_desc,
                            position: 'top-right'
                        });
                        post.likes.push({});
                        post.liked = true;
                    }

                    if (like.error_type === 'warning') {
                        this.$q.notify({
                            type: 'warning',
                            message: like.error_desc,
                            position: 'top-right'
                        })
                    }
                }
            })
        },

        async deleteLike(id) {
            this.posts.filter(async post => {
                if (post.post_id === id) {
                    const likeFetch = await fetch('https://localhost:5000/my/dislike', {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json',
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                        },
                        body: JSON.stringify({
                            post_id: id
                        })
                    });

                    const dislike = await likeFetch.json()

                    if (dislike.error_type === 'positive') {
                        this.$q.notify({
                            type: 'positive',
                            message: dislike.error_desc,
                            position: 'top-right'
                        });
                        post.likes.pop();
                        post.liked = false;
                    }
                }
            })
        },

        async loadMore() {
            this.page += 1;

            const postsFetch = await fetch(`https://localhost:5000/post/gposts/${this.page}`, {
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            });
            const posts = await postsFetch.json();

            posts.forEach(async post => {
                post.picture = post.picture.replace("b'", 'data:image/png;base64,');
                post.picture = post.picture.replace("'", '');

                if (post.creator.picture !== '1' && post.creator.picture !== '') {
                    post.creator.picture = post.creator.picture.replace("b'", 'data:image/png;base64,');
                    post.creator.picture = post.creator.picture.replace("'", '');
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