<template>
    <q-page class="flex flex-center">
        <div id="main">
            <div id="left">
                <q-list id="chat-list">
                    <router-link v-for="chat in chats" :to="'/inside/chats/'+chat.partner.id" :key="chat.chat_id">
                        <q-item class="chat-item" clickable v-ripple>
                            <q-item-section avatar v-if="chat.partner.picture == 1" style="padding-left: 5%;">
                                <q-icon name='person' />
                            </q-item-section>
                            <q-item-section avatar v-else style="padding-left: 2%;">
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
                <div style="padding-top: 5%; display: flex; justify-content: space-between;" v-if="chats.length == 0">
                    <h5>Todavía no hay chats creados</h5>
                    <router-link to="/inside/search">
                        <q-btn color='black' push label="BUSCAR USUARIOS"/>
                    </router-link>
                </div>
                <router-view v-else />
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
                        id: 0,
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
        const userFetch = await fetch('https://localhost:5000/my/getProfile', {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const user = await userFetch.json();

        this.user = user.user_id;
        
        const chatsFetch = await fetch('https://localhost:5000/chat/getChats', {
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        });

        const chats = await chatsFetch.json()

        chats.forEach(async a => {
            if (a.partner.picture !== '1' && a.partner.picture !== '') {
                const profilePicFetch = await fetch('https://localhost:5000/my/image', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(a.partner.picture)
                })

                const profilePic = await profilePicFetch.json();
                profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
                profilePic.picture = profilePic.picture.replace("'", '');
                a.partner.picture = profilePic.picture;
            }
        });

        this.chats = chats;
    },
    methods: {
        async deleteChat(id) {
            const deleteFetch = await fetch('https://localhost:5000/chat/deleteChat', {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                body: JSON.stringify({
                    chat_id: id
                })
            });

            const deleteResp = await deleteFetch.json();

            if (deleteResp.type === 'positive') {
                this.$q.notify({
                    type: 'warning',
                    message: deleteResp.message,
                    position: 'top-right'
                })

                this.$router.push('/inside')
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