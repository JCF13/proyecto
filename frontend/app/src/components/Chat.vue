<template>
    <div class="q-pa-md row justify-center">
        <div style="width: 100%; max-width: 600px; padding: 5% 0;">
            <div v-for="message in messages" :key="message.id">
                <div v-if="message.creator.id == creator.id" style="margin-bottom: 1%">
                    <q-chat-message
                        :text="[message.message]"
                        stamp="7 minutes ago"
                        size="5"
                        sent
                        bg-color="grey-2"
                    />
                </div>

                <div v-else style="margin-bottom: 1%">
                    <q-chat-message
                        :text="[message.message]"
                        stamp="7 minutes ago"
                        size="5"
                        bg-color="blue-grey-1"
                    />
                </div>
            </div>
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
                }
            ]
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
</style>