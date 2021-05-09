<template>
    <q-layout view="hHh LpR fFf" id="layout">        
        <q-page-container id="container">
            <router-view />
        </q-page-container>
        <q-footer elevated class="text-white" id="footer">
            <q-tabs v-model="tab" class="text-black col-md-12">
                <router-link to="/inside/home" class="col-md-1">
                    <q-tab name="home" icon="home"/>
                </router-link>
                <router-link to="/inside/search" class="col-md-1">
                    <q-tab name="search" icon="search" />
                </router-link>
                <q-tab class="col-md-1" name="new-post" icon="add_circle" @click="postDialog = true" />
                <router-link to="/inside/chats" class="col-md-1">
                    <q-tab name="chats" icon="chat_bubble_outline">
                    <q-badge floating color="negative">9</q-badge></q-tab>
                </router-link>
                <router-link to="/inside/notifications" class="col-md-1">
                    <q-tab name="notifications" icon="notifications">
                        <q-badge floating color="negative">12</q-badge>
                    </q-tab>
                </router-link>
                <router-link to="/inside/profile" class="col-md-1">
                    <q-tab name="profile" icon="person"/>
                </router-link>
            </q-tabs>
        </q-footer>

        <q-dialog v-model="postDialog" position="bottom" id="upload-dialog">
            <q-card style="width: 300px">
                <router-link to="/inside/camera">
                    <q-card-section class="row items-center no-wrap">
                        <div class="flex d-flex justify-between align-items-center col-md-12">
                            <q-icon size="30px" name="photo_camera"/>
                            <p>HACER FOTO</p>
                        </div>
                    </q-card-section>
                </router-link>
                <q-separator/>
                <q-card-section class="row items-center no-wrap" @click="uploadDialog = true">
                        <div class="flex d-flex justify-between col-md-12">
                            <q-icon size="30px" name="file_upload"/> 
                            <p>SUBIR FOTO</p>
                        </div>
                </q-card-section>
            </q-card>
        </q-dialog>

        <q-dialog v-model="uploadDialog">
            <q-card style="width: 700px; max-width: 80vw;">
                <q-card-section>
                    <div class="text-h6">Sube una foto con la que crear una publicación</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                    <q-uploader style="width:100%"
                        url="http://localhost:4444/upload"
                    />
                </q-card-section>

                <q-card-actions align="right" class="bg-white">
                    <q-btn flat label="SIGUIENTE" @click="goToPost" />
                </q-card-actions>
            </q-card>
        </q-dialog>
    </q-layout>
</template>

<script>
export default {
    data () {
        return {
            tab: '',
            postDialog: false,
            uploadDialog: false,
            model: null
        }
    },
    methods: {
        goToPost() {
            this.$router.push('/inside/new-post')
        }
    }
}
</script>

<style scoped>
    a {
        color: black;
        text-decoration: none;
    }

    #layout {
        background: #b3e5fc;
    }

    #upload-dialog div:hover {
        cursor: pointer;
    }

    footer {
        background: linear-gradient(to left, #4fc3f7, #b2ff59)
    }
</style>