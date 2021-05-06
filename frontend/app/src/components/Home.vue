<template>
    <q-page class="flex flex-center" id="page">        
        <div id="main" class="flex flex-center">
            <q-card class="my-card" v-for="image in images" :key="image.img">
                <q-item class="card-top">
                    <q-item-section avatar>
                    <q-avatar>
                        <img src="https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg">
                    </q-avatar>
                    </q-item-section>

                    <q-item-section>
                    <q-item-label>Nombre de usuario</q-item-label>
                    <q-item-label caption>Pie de foto</q-item-label>
                    </q-item-section>

                    <q-item-section align="right" class="info-post">
                        <q-item-label>
                            4 <q-icon name="comment"/>
                        </q-item-label>
                        <q-item-label>
                            10 <q-icon name="favorite" color="red"/>
                            </q-item-label>
                    </q-item-section>
                </q-item>

                <img :src="image.img" @click="openPost">
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
    data() {
        return {
            images: [
                {
                    "img": "https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg"
                },
                {
                    "img": "https://ugc.kn3.net/i/760x/http://wackymania.com/image/2011/6/vertical-panoramic-photography/vertical-panoramic-photography-06.jpg"
                },
                {
                    "img": "https://i.pinimg.com/originals/c2/88/c7/c288c7ff9eae9c9f7397115b140fb2b5.jpg"
                }
            ],
        }
    },
    methods: {
        openPost() {
            this.$router.push('/inside/home/post')
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
        border-bottom: 1px solid rgb(128, 128, 128);
    }

    .info-post {
        padding-right: 1%;
    }

    a {
        text-decoration: none;
    }

</style>