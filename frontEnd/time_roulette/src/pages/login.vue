<script setup lang="ts">
import LoginDiv from '../components/login.vue'
</script>

<template>
  <LoginDiv class="login" activeName="first"/>
</template>

<style scoped>
.login{
    display: flex;
    justify-content: center;
}
body{
    margin: 0;
}

</style>