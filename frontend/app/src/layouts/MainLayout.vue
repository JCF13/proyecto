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
                <router-link to="/inside/camera" class="col-md-1">
                    <q-tab name="new-post" icon="add_circle" />
                </router-link>
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
    </q-layout>
</template>

<script>
export default {
    data () {
        return {
            tab: '',
            postDialog: false,
            model: null
        }
    },
    created() {
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