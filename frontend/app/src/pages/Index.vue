<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-full.svg"
      @dblclick="go_network"
    >
  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',
  methods: {
    go_network() {
      this.$router.push('/redsocial/main')
    }
  }
}
</script>
