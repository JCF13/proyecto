<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App'
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;700&display=swap');

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Nunito', sans-serif;
  }
  
  #q-app {
    height: 100%;
    background: rgb(243, 243, 243);
  }
</style>
