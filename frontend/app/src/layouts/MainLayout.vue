<template>
  <q-layout view="hHh lpR fFf" id="layout">
    <q-page-container id="container">
      <router-view />
    </q-page-container>
    <q-footer elevated class="bg-white text-white">
            <q-toolbar class="row d-flex justify-content-center">
                <q-tabs class="col-md-12">
                    <router-link to="/inside/home" class="col-md-1">
                        <q-tab name="tab1" icon="home" />
                    </router-link>
                    <router-link to="/inside/search" class="col-md-1">
                        <q-tab name="tab2" icon="search" />
                    </router-link>
                    <router-link to="/inside/new-post" class="col-md-1">
                        <q-tab name="tab4" icon="add_circle" />
                    </router-link>
                    <router-link to="/inside/camera" class="col-md-1">
                        <q-tab name="tab3" icon="photo_camera" />
                    </router-link>
                    <router-link to="/inside/profile" class="col-md-1">
                        <q-tab name="tab5" icon="person" />
                    </router-link>
                </q-tabs>
            </q-toolbar>
        </q-footer>
  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      tab: ''
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
    background: rgb(243, 243, 243);
  }
</style>