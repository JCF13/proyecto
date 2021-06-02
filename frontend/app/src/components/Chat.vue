<template>
    <div id="main-chat">
        <div id="messages">
            <div v-for="message in chat.messages" :key="message.message_id">
                <div v-if="(partner == chat.creator.user_id) && (message.created_by == partner)" style="margin-bottom: 1%">
                    <q-chat-message :id="message.message_id"
                        :text="[message.message]"
                        :stamp="[message.created_on]"
                        size="5"
                        bg-color="blue-grey-1"
                    />
                </div>
                <div v-else style="margin-bottom: 1%">
                    <q-chat-message :id="'message'+message.message_id"
                        :text="[message.message]"
                        :stamp="[message.created_on]"
                        size="5"
                        sent
                        bg-color="grey-2"
                    />
                </div>
            </div>
        </div>
        <div>
            <q-input color="black" v-model="message">
                <template v-slot:append>
                    <q-icon color="black" name="send" @click="sendMessage"/>
                </template>
            </q-input>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            chat: {
                chat_id: 0,
                creator: {
                    user_id: 0,
                    username: '',
                    picture: ''
                },
                partner: {
                    user_id: 0,
                    username: '',
                    picture: ''
                },
                messages: [{
                    message_id: 0,
                    created_by: 0,
                    created_on: '',
                    message: ''
                }]
            },
            message: '',
            partner: 0
        }
    },
    async created() {
        const partner = this.$route.params.id;
        this.partner = partner;

        const chatFetch = await fetch(`http://localhost:5000/chat/getChat/${partner}`, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('access_token')
            }
        })

        const chat = await chatFetch.json();

        this.chat = chat;
    },
    methods: {
        sendMessage() {
            console.log(document.querySelector('#messages').offsetHeight)
            this.messages.push({
                id: 14,
                creator: {
                    id: 1,
                },
                message: this.message
            });

            document.querySelector('#messages').scrollTop = document.querySelector('#messages').scrollHeight;

        },
    },
}
</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #main-chat {
        display: grid;
        grid-template-rows: 88% 12%;
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 100%;
        padding-top: 2%;
    }

    #messages {
        height: 100%; 
        width: 100%; 
        overflow-y: scroll;
    }

    #messages::-webkit-scrollbar {
        display: none;
    }


</style>