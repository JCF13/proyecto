<template>
    <q-page class="flex flex-center" id="page">        
        <div id="main" class="flex flex-center">
            <q-card class="my-card" v-for="post in posts" :key="post.id">
                <q-item class="card-top">
                    <q-item-section avatar>
                        <q-avatar>
                            <img :src="post.creator.profilePic" alt="">
                        </q-avatar>
                    </q-item-section>

                    <q-item-section>
                        <q-item-label>{{post.creator.username}}</q-item-label>
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

                <img :src="post.photo" @click="openPost(post.id)" @dblclick="sendLike">
            </q-card>
            
            <div id="more">
                <q-icon name="add_circle_outline" size="30px"/>
            </div>
        </div>
        <router-view/>
    </q-page>
</template>

<script>
export default {
    // "https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg"
    // "https://ugc.kn3.net/i/760x/http://wackymania.com/image/2011/6/vertical-panoramic-photography/vertical-panoramic-photography-06.jpg"
    // "https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg"
    
    data() {
        return {
            posts: [
                {
                    id: 1,
                    photo: "https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg",
                    caption: 'Pie de foto',
                    creationDate: '14/05/2021',
                    creator: {
                        id: 1,
                        username: 'Nombre_de_usuario',
                        profilePic: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg'
                    },
                    comments: [
                        {
                            id: 1,
                            user: {
                                id: 2,
                                username: 'Nombre_de_usuario2'
                            },
                            message: 'Comentario 1',
                            creationDate: '15/05/2021'
                        }
                    ],
                    likes: [
                        {
                            id: 1,
                            user: {
                                id: 2,
                                username: 'Nombre_de_usuario2'
                            }
                        },
                    ]
                }
            ],
        }
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/home/post/${id}`)
        },
        sendLike() {
            
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