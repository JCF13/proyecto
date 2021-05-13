<template>
    <div id="main-chat">
        <div id="messages">
            <div v-for="message in messages" :key="message.id">
                <div v-if="message.creator.id == creator.id" style="margin-bottom: 1%">
                    <q-chat-message :id="'message'+message.id"
                        :text="[message.message]"
                        stamp="7 minutes ago"
                        size="5"
                        sent
                        bg-color="grey-2"
                    />
                </div>

                <div v-else style="margin-bottom: 1%">
                    <q-chat-message :id="message.id"
                        :text="[message.message]"
                        stamp="7 minutes ago"
                        size="5"
                        bg-color="blue-grey-1"
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
            creator: {
                id: 1,
            },
            partner: {
                id: 2,
            },
            messages: [
                {
                    id: 1,
                    creator: {
                        id: 1,
                    },
                    message: 'Hey, how are you?'
                },
                {
                    id: 2,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 3,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 4,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 5,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 6,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 7,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 8,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 9,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 10,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 11,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 12,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                },
                {
                    id: 13,
                    creator: {
                        id: 2,
                    },
                    message: 'Fine, hoy are you?'
                }
            ],
            message: ''
        }
    },
    methods: {
        sendMessage() {
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