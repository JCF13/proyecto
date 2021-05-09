<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="left">
                <q-list id="chat-list">
                    <router-link v-for="(chat,count) in chats" :to="'/inside/chats/'+chat.partner.id" :key="chat.id" >
                        <q-item class="chat-item" clickable v-ripple @click="selectChat(count)" :active="chat.active" 
                            active-class="bg-grey text-white">
                            <q-img
                                :src="chat.partner.profilePic" class="bg-white"
                                style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                                    border-radius:50%; border: 1px solid black; margin: 5%;"
                                contain
                            />

                            <q-item-section>{{chat.partner.username}}</q-item-section>

                            <q-item-section side>
                                <q-icon @click="deleteChat(chat.id)" name="delete" style="font-size:30px; color:red; display:none"/>
                            </q-item-section>
                        </q-item>
                        <q-separator/>
                    </router-link>
                </q-list>
            </div>
            <div id="right">
                <router-view/>
            </div>
        </div>
    </q-page>
</template>

<script>
export default {
    data() {
        return {
            chats: [
                {
                    id: 1,
                    partner: {
                        id: 2,
                        username: 'Nombre_usuario_2',
                        profilePic: 'https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg'
                    },
                    active: false
                },
                {
                    id: 2,
                    partner: {
                        id: 3,
                        username: 'Nombre_usuario_3',
                        profilePic: 'https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg'
                    },
                    active: false
                },
                {
                    id: 3,
                    partner: {
                        id: 4,
                        username: 'Nombre_usuario_4',
                        profilePic: 'https://ugc.kn3.net/i/760x/http://wackymania.com/image/2011/6/vertical-panoramic-photography/vertical-panoramic-photography-06.jpg'
                    },
                    active: false
                },
            ]
        }
    },
    methods: {
        selectChat(index) {
            this.chats.forEach((a, i) => {
                if (i == index) {
                    a.active = true
                } else a.active = false
            })
        },
        deleteChat(id) {
            console.log(id)
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
        height: 80vh;
        width: 60%;
        box-shadow: 0 0 10px rgb(214, 214, 214);
        display: grid;
        grid-template-columns: 25% 75%;
    }

    #left {
        overflow-y: scroll;
        border-right: 1px solid black;
    }

    #left::-webkit-scrollbar {
        display: none;
    }
    
    a {
        text-decoration: none;
        color: black;
    }

    #right {
        margin: 0 auto;
        width: 90%;
        height: 100%;
    }

    .avatar-chat {
        border-radius: 50%;
    }

    img {
        border: 1px solid black;
    }

    hr {
        background: black;
    }

    .chat-item:hover i {
        display: block !important;
    }
</style>