<template>
    <q-dialog v-model="dialog" persistent>
        <q-card id="my-card">
            <q-card-section horizontal>
                <div id="card-left">
                    <q-icon id="close" name="highlight_off" size="30px" @click="close" />

                    <img id="image" :src="post.photo" alt="">

                    <div id="pie-de-foto" class="absolute-bottom text-subtitle2">
                        {{post.caption}}
                    </div>
                </div>

                <q-card-actions vertical id="card-right">
                    <div id="modal-user">
                        <q-avatar size="30px" class="avatar">
                            <img :src="post.creator.profilePic" alt="">
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
                        <p>{{post.creationDate}}</p>
                    </div>
                    <div id="comments">
                        <div v-for="comment in post.comments" :key="comment.id">
                            <q-avatar size="20px" class="avatar">
                                <img :src="comment.user.profilePic" alt="">
                            </q-avatar>
                            <p>
                                <span>{{comment.user.username}}.</span>
                                {{comment.message}}
                            </p>
                        </div>
                        <q-icon v-if="post.comments.length>5" name="add_circle_outline" size="25px" />
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
                id: 1,
                creationDate: '15/04/2021',
                photo: 'https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg',
                caption: 'Pie de foto',
                creator: {
                    id: 1,
                    username: 'Nombre_de_usuario',
                    profilePic: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg'
                },
                likes: [
                    {
                        id: 1,
                        user: {
                            id: 2,
                            username: 'Nombre_usuario_2',
                            profilePic: 'https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg'
                        }
                    }
                ],
                comments: [
                    {
                        id: 1,
                        user: {
                            id: 2,
                            username: 'Nombre_usuario_2',
                            profilePic: 'https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg'
                        },
                        creationDate: '15/04/2021',
                        message: 'Comentario1'
                    }
                ]
            },
            user: {
                id: null,
            },
            message: null
        }
    },
    created() {
        const postId = this.$route.params.id;

        //getPost(postId);
    },
    methods: {
        close() {
            this.$router.go(-1)
        },

        // Cargar post
        async getPost(id) {
            const postFetch = await fetch(`http://localhost:5000/private/post/${id}`)
            const post = postFetch.json();

            this.post = post;
        },

        // Enviar comentario y nueva notificación
        async newComment() {
            const postId = this.$route.params.id;
            
            const comment = await fetch('http://localhost:5000/private/post/comment', {
                method: 'POST',
                body: JSON.stringify({
                    post: postId,
                    creator: this.post.creator.id,
                    user: this.user.id,
                    message: this.message
                })
            });
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