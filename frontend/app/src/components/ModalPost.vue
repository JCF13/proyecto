<template>
    <q-dialog v-model="dialog" persistent>
        <q-card id="my-card">
            <q-card-section horizontal>
                <div id="card-left">
                    <q-icon id="close" name="highlight_off" size="30px" @click="close" />

                    <img id="image" :src="post.picture" alt="">

                    <div id="pie-de-foto" class="absolute-bottom text-subtitle2">
                        {{post.caption}}
                    </div>
                </div>

                <q-card-actions vertical id="card-right">
                    <div id="modal-user">
                        <q-avatar v-if="post.creator.picture === '1'">
                            <q-icon name='person' />
                        </q-avatar>
                        <q-avatar v-else size="30px" class="avatar">
                            <img :src="post.creator.picture" alt="">
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
                    <div>
                        <q-list>
                            <q-item v-for="comment in post.comments" :key="comment.id">
                                <q-item-section avatar>
                                <q-avatar v-if="comment.user.picture == 1">
                                    <q-icon name='person' />
                                </q-avatar>
                                <q-avatar v-else>
                                    <img :src="comment.user.picture" />
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
                    user_id: 0,
                    username: '',
                    picture: ''
                },
                likes: [
                    {
                        id: 0,
                        user: {
                            user_id: 0,
                            username: '',
                            picture: ''
                        }
                    }
                ],
                comments: [
                    {
                        id: 0,
                        user: {
                            user_id: 0,
                            username: '',
                            picture: ''
                        },
                        creationDate: '',
                        message: ''
                    }
                ]
            },
            user: {
                id: null,
            },
            message: null
        }
    },
    async created() {
        const postId = this.$route.params.id;
        const postFetch = await fetch(`http://localhost:5000/post/gpost/${postId}`, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
            }
        });
        const post = await postFetch.json();

        const imgFetch = await fetch('http://localhost:5000/my/image', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify(post.picture)
        })
        const img = await imgFetch.json()

        post.created_on = post.created_on.split('.')[0].replace('T', ' ')

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

        this.post = post;
    },
    methods: {
        close() {
            this.$router.go(-1)
        },

        async newComment() {
            const postId = this.$route.params.id;
            
            const commentFetch = await fetch('http://localhost:5000/my/comment', {
                method: 'PATCH',
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({
                    post_id: postId,
                    message: this.message
                })
            });

            const comment = await commentFetch.json()

            if (comment.type === 'positive') {
                this.$q.notify({
                    type: 'positive',
                    message: comment.message,
                    position: 'top-right'
                })
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

    #comments {
        grid-area: comments;
        display: grid;
    }

    #comments div {
        display: grid;
        grid-template-columns: 10% 90%;
        margin-bottom: 5%;
    }

    #comments i:last-child {
        justify-self: center;
    }

    #pie-de-foto {
        background: rgba(0, 0, 0, 0.692);
        width: 50%;
        color: white;
        text-align: left;
        padding: 1%;
        height: 7%;
    }

    #new-comment {
        grid-area: comment;
    }

</style>