<template>
    <q-layout view="hHh LpR fFf" id="layout">        
        <q-page-sticky position="top-right" :offset="[40, 20]" id="notifications">
            <q-btn color="black" icon="notifications" glossy rounded>
                <q-menu transition-show="flip-right" transition-hide="flip-left">
                    <q-list style="max-width: 100%; max-height: 350px" >
                        <q-slide-item @right="onRight">
                            <template v-slot:left>
                                <q-icon name="done" />
                            </template>
                            <template v-slot:right>
                                <q-icon name="alarm" />
                            </template>

                            <q-item>
                                <q-item-section avatar>
                                    <q-avatar color="primary" text-color="white" icon="bluetooth" />
                                </q-item-section>
                                <q-item-section>Icons only</q-item-section>
                            </q-item>
                        </q-slide-item>
                        <q-slide-item @right="onRight">
                            <template v-slot:left>
                                <q-icon name="done" />
                            </template>
                            <template v-slot:right>
                                <q-icon name="alarm" />
                            </template>

                            <q-item>
                                <q-item-section avatar>
                                    <q-avatar color="primary" text-color="white" icon="bluetooth" />
                                </q-item-section>
                                <q-item-section>Icons only</q-item-section>
                            </q-item>
                        </q-slide-item>
                    </q-list>
                </q-menu>
            </q-btn>
        </q-page-sticky>
        <q-page-container id="container">
            <router-view />
        </q-page-container>
        <q-footer elevated class="bg-white text-white">
            <q-tabs v-model="tab" class="text-black col-md-12">
                <router-link to="/inside/home" class="col-md-1">
                    <q-tab name="home" icon="home"/>
                </router-link>
                <router-link to="/inside/search" class="col-md-1">
                    <q-tab name="search" icon="search" />
                </router-link>
                <router-link to="/inside/camera" class="col-md-1">
                    <q-tab name="camera" icon="photo_camera" />
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
      left: true
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
    z-index: 0;
  }

  #layout::-webkit-scrollbar {
    display: none;
  }

  #notifications {
    z-index: 1;
  }

</style>