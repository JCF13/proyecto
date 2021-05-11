<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="top">
                <div id="left-top">
                    <q-img
                        :src="user.profilePic"
                        style="width:100%; max-width: 200px; height:100%; max-height: 175px; border-radius:50%; border: 2px solid black;"
                        contain
                    />
                </div>
                <div id="right-top">
                    <q-card class="my-card" flat>
                        <q-card-section vertical>
                            <q-card-section horizontal class="d-flex justify-between">
                                <h5>{{user.username}}</h5>

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
                                <q-btn class="bg-white" push label="SEGUIR" />
                                <q-btn class="bg-white" push label="DEJAR DE SEGUIR" style="display:none" />
                                <q-btn class="bg-white" push label="TE SIGUE" />
                            </q-card-section>
                        </q-card-section>
                    </q-card>
                </div>
            </div>

            <div v-if="user.posts.length>0" id="publicaciones">
                <div v-for="post in user.posts" :key="post.id" @click="openPost(post.id)">
                    <img class="img-post" :src="post.photo" alt="" >
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
                id: 1,
                username: 'Nombre_de_usuario',
                profilePic: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg',
                followers: 2,
                following: 4,
                posts: [
                    {
                        id: 1,
                        photo: 'https://ugc.kn3.net/i/760x/http://wackymania.com/image/2011/6/vertical-panoramic-photography/vertical-panoramic-photography-06.jpg',
                        caption: 'Pie de foto',
                        likes: 4,
                        comments: 2
                    },
                    {
                        id: 2,
                        photo: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg',
                        caption: 'Pie de foto',
                        likes: 4,
                        comments: 2
                    },
                    {
                        id: 3,
                        photo: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg',
                        caption: 'Pie de foto',
                        likes: 4,
                        comments: 2
                    },
                    {
                        id: 3,
                        photo: 'https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg',
                        caption: 'Pie de foto',
                        likes: 4,
                        comments: 2
                    }
                ],
            },            
        }
    },
    methods: {
        openPost(id) {
            this.$router.push(`/inside/profile/post/${id}`)
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
