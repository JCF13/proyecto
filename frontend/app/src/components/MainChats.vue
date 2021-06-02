<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="left">
                <q-list id="chat-list">
                    <router-link v-for="chat in chats" :to="'/inside/chats/'+chat.partner.user_id" :key="chat.chat_id" >
                        <q-item class="chat-item" clickable v-ripple @click="selectChat(chat.chat_id)" :active="chat.active" 
                            active-class="bg-grey text-white">
                            <q-item-section avatar v-if="chat.partner.picture == 1">
                                <q-icon name='person' />
                            </q-item-section>
                            <q-item-section avatar v-else>
                                <q-img
                                    :src="chat.partner.picture" class="bg-white"
                                    style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                                        border-radius:50%; border: 1px solid black; margin: 5%;"
                                    contain
                                />
                            </q-item-section>
                            

                            <q-item-section>{{chat.partner.username}}</q-item-section>

                            <q-item-section side>
                                <q-icon @click="deleteChat(chat.chat_id)" name="delete" style="font-size:30px; color:red; display:none"/>
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
                    id: 0,
                    partner: {
                        user_id: 0,
                        username: '',
                        picture: ''
                    },
                    active: false
                },
            ],
            user: 0
        }
    },
    async created() {
        const userFetch = await fetch('http://localhost:5000/my/getProfile', {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const user = await userFetch.json();

        this.user = user.user_id;
        
        const chatsFetch = await fetch('http://localhost:5000/chat/getChats', {
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const chats = await chatsFetch.json()

        chats.forEach(a => {
            if (this.user === a.partner) {
                console.log('si')
            }
        })

        this.chats = chats;
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
        border-radius: 5px;
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
        position: relative;
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