<template>
    <div id="notifications-layout">
        <h4>Notificaciones pendientes</h4>
        <q-list id="notifications-list">
            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="favorite" color="red" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 ha dado Me Gusta</q-item-section>
                    <q-icon name="close"/>
                </q-item>
            </q-slide-item>
            
            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="comment" color="blue" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 ha comentado</q-item-section>
                    <q-icon name="close"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="person_add" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha seguido</q-item-section>
                    <q-icon name="close"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>

            <q-slide-item @left="deleteNotification" left-color="red">
                <template v-slot:left >
                    <q-icon left name="delete"/>
                </template>
                <q-item>
                    <q-item-section avatar>
                        <q-icon name="waving_hand" color="black" size="30px"/>
                    </q-item-section>
                    <q-item-section>Usuario1 te ha dejado de seguir</q-item-section>
                    <q-icon name="close" class="justify-center"/>
                </q-item>
            </q-slide-item>
        </q-list>
    </div>
</template>

<script>
export default {
    data() {
        return {

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

    #notifications-layout {
        max-height: 80vh;
        width: 50%;
        margin: 0 auto;
        padding: 2%;
    }

    #notifications-list {
        margin-top: 2%;
        height: 70vh;
        overflow-y: scroll;
    }

    #notifications-list::-webkit-scrollbar {
        display: none;
    }

    .q-slide-item {
        background: rgb(243, 243, 243);
    }
</style>