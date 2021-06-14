<template>
    <q-dialog v-model="dialog" persistent>
        <q-card id="my-card">
            <q-card-section horizontal>
                <div id="card-left">
                    <q-icon id="close" name="highlight_off" size="30px" @click="close" />
                    <q-icon v-if="post.creator.id === user.id" id="delete" color='red' name='delete' size='30px' @click="deletePost" />

                    <img id="image" :src="post.picture" alt="publicacion">

                    <div id="pie-de-foto" class="absolute-bottom text-subtitle2">
                        {{post.caption}}
                    </div>
                </div>

                <q-card-actions vertical id="card-right">
                    <div id="modal-user">
                        <q-avatar v-if="post.creator.picture === '1' || post.creator.picture === ''">
                            <q-icon name='person' />
                        </q-avatar>
                        <q-avatar v-else size="30px" class="avatar">
                            <img :src="post.creator.picture" alt="foto_de_perfil">
                        </q-avatar>
                        <h6>{{post.creator.username}}</h6>
                    </div>
                    <div id="modal-info">
                        <div>
                            <p>{{post.likes.length}}</p>
                            <q-icon size="15px" name="favorite" color="red" />
                        </div>
                        <div>
                            <p>{{post.comments.length}}</p>
                            <q-icon size="15px" name="comment" color="blue" />
                        </div>
                    </div>
                    <div id="creation-date">
                        <p>{{post.created_on}}</p>
                    </div>
                    <div id="comments">
                        <q-list id="comments-post">
                            <q-item v-for="comment in post.comments" :key="comment.id">
                                <q-item-section avatar>
                                <q-avatar v-if="comment.user.picture === '1' || comment.user.picture === ''">
                                    <q-icon name='person' />
                                </q-avatar>
                                <q-avatar v-else>
                                    <img :src="comment.user.picture" alt="foto_de_perfil" />
                                </q-avatar>
                                </q-item-section>
                                <q-item-section>{{comment.message}}</q-item-section>
                            </q-item>
                        </q-list>
                    </div>
                    <div id="new-comment">
                        <q-input label="Escribe un comentario" color="black" v-model="message">
                            <template v-slot:append>
                                <q-icon name="send" color="black" @click="newComment"/>
                            </template>
                        </q-input>
                    </div>
                </q-card-actions>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<script>
export default {
    data() {
        return {
            dialog: true,
            post: {
                post_id: 0,
                created_on: '',
                picture: '',
                caption: '',
                creator: {
                    id: 0,
                    username: '',
                    picture: ''
                },
                likes: [
                    {
                        id: 0,
                        user: {
                            id: 0,
                            username: '',
                            picture: ''
                        }
                    }
                ],
                comments: [
                    {
                        id: 0,
                        user: {
                            id: 0,
                            username: '',
                            picture: ''
                        },
                        creationDate: '',
                        message: ''
                    }
                ]
            },
            user: null,
            message: null
        }
    },
    async created() {
        const userFetch = await this.$axios.get('https://localhost:5000/my/getProfile',
        {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const user = userFetch.data;

        this.user = user;
        
        const postId = this.$route.params.id;
        
        const postFetch = await this.$axios.get(`https://localhost:5000/post/gpost?id=${postId}`,
        {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const post = postFetch.data;

        post.created_on = post.created_on.split('.')[0].replace('T', ' ')

        post.picture = post.picture.replace("b'", 'data:image/png;base64,');
        post.picture = post.picture.replace("'", '');

        if (post.creator.picture !== '1' && post.creator.picture !== '') {
            post.creator.picture = post.creator.picture.replace("b'", 'data:image/png;base64,');
            post.creator.picture = post.creator.picture.replace("'", '');
        }

        post.comments.forEach(a => {
            if (a.user.picture !== '1' && a.user.picture !== '') {
                a.user.picture = a.user.picture.replace("b'", 'data:image/png;base64,');
                a.user.picture = a.user.picture.replace("'", '');
            }
        })

        this.post = post;
    },
    methods: {
        close() {
            this.$router.go(-1)
        },

        async newComment() {
            const postId = this.$route.params.id;
            
            const commentFetch = await this.$axios.patch('https://localhost:5000/my/comment',
            {
                post_id: postId,
                message: this.message
            },
            {
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                }
            });

            const comment = commentFetch.data;

            if (comment.error_type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: comment.error_desc,
                    position: 'top-right'
                });

                this.comments.push({
                    id: 0,
                    user: {
                        id: 0,
                        username: '',
                        picture: this.user.picture
                    },
                    creationDate: '',
                    message: comment.message
                })
            }
        },

        async deletePost() {
            const deleteFetch = await this.$axios.post(`https://localhost:5000/post/deletepost/${this.post.post_id}`,
            {},
            {
                headers: {
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

                this.$router.push('/inside/')
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

    #my-card {
        width: 100%;
        max-width: 800px;
    }


    #image {
        justify-self: center;
        max-width: 400px;
        max-height: 500px;
        align-self: center;
    }

    #card-left {
        display: grid;
        width: 50%;
        height: 500px;
        border-right: 2px solid grey;
        margin: 0 auto;
    }

    #card-right {
        padding: 1%;
        width: 50%;
        display: grid;
        grid-template-columns: 50% 50%;
        grid-template-rows: 10% 10% 70% 10%;
        grid-template-areas: 
            "user info"
            "fecha fecha"
            "comments comments"
            "comment comment";
    }

    #card-right img {
        object-fit: contain;
        border: 2px solid black;
    }

    #modal-user {
        grid-area: user;
        display: grid;
        grid-template-columns: 20% 80%;
    }

    #modal-info {
        padding-right: 5%;
        grid-area: info;
        display: grid;
        grid-template-rows: 50% 50%;
        justify-items: right;
    }

    #modal-info div:first-child {
        display: grid;
        grid-template-columns: 90% 10%;
    }

    #modal-info div:last-child {
        display: grid;
        grid-template-columns: 90% 10%;
    }

    #creation-date {
        grid-area: fecha;
    }

    span {
        font-weight: bold;
    }

    #close {
        position: absolute;
        margin: 1%;
    }

    #close {
        cursor: pointer;
    }

    #delete {
        cursor: pointer;
        position: absolute;
        right: 50%;
        margin: 1%;
    }

    #comments {
        grid-area: comments;
    }

    #pie-de-foto {
        background: rgba(0, 0, 0, 0.692);
        width: 50%;
        color: white;
        text-align: left;
        padding: 1%;
        height: 7%;
    }

    #comments-post {
        grid-area: comments;
        overflow-y: scroll;
        overflow-x: hidden;
        max-height: 80%;
        max-width: 100%;
    }

    #comments-post::-webkit-scrollbar {
        display: none;
    }

    #new-comment {
        grid-area: comment;
    }

</style>