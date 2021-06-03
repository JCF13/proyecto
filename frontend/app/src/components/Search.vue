<template>
    <q-layout view="hHh lpR fFf" id="social-layout">
        <div id="menu-search">
            <q-toolbar class="row d-flex justify-content-center">
                <q-input color="grey-3" class="col-sm-12" v-model="searchBy" label="Buscar usuario" @input="search">
                    <template v-slot:append>
                        <q-icon name="person_search" color="black" />
                    </template>
                </q-input>
            </q-toolbar>
            <q-list>
                <q-item v-for="user in results" :key="user.user_id">
                    <q-item-section avatar>
                        <q-avatar v-if="user.picture == 1">
                            <q-icon name='person' />
                        </q-avatar>
                        <q-avatar v-else>
                            <q-img
                                    :src="user.picture" class="bg-white"
                                    style="width:30px; max-width: 30px; height:30px; max-height: 30px; 
                                        border-radius:50%; border: 1px solid grey; margin: 5%;"
                                    contain
                                />
                        </q-avatar>
                    </q-item-section>
                    <q-item-section>{{user.username}}</q-item-section>
                    <q-item-section side>
                        <router-link class="ver-perfil" :to='"/inside/user/" + user.username'>
                            <q-btn label="VER PERFIL" color="black"/>
                        </router-link>
                    </q-item-section>
                </q-item>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
export default {
    data() {
        return {
            searchBy: '',
            results: []
        }
    },
    methods: {
        async search() {
            if (this.searchBy.length >= 3) {
                const searchFetch = await fetch('http://localhost:5000/my/searchUsers', {
                    method: 'POST',
                    headers: {
                        'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify({
                        search: this.searchBy
                    })
                });

                const search = await searchFetch.json();

                if (search.length > 0) {
                    search.forEach(async a => {
                        const profilePicFetch = await fetch('http://localhost:5000/my/image', {
                            method: 'POST',
                            headers: {
                                'Content-type': 'application/json'
                            },
                            body: JSON.stringify(a.picture)
                        })

                        const profilePic = await profilePicFetch.json();
                        profilePic.picture = profilePic.picture.replace("b'", 'data:image/png;base64,');
                        profilePic.picture = profilePic.picture.replace("'", '');
                        a.picture = profilePic.picture;
                    })

                    this.results = search;
                } else {
                    this.$q.notify({
                        type: 'warning',
                        message: 'No se han encontrado resultados',
                        position: 'top'
                    })
                }

            }
            
        }
    }
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #social-layout {
        height: 100%;
        width: 70%;
        margin: 0 auto;
        padding: 2%;
    }

    a {
        text-decoration: none;
        color: black;
    }

    #menu-search {
        background: white;
        box-shadow: 0 0 10px rgb(161, 161, 161);
        border-radius: 10px;
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
        padding: 1%;
    }

</style>