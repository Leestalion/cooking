<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterView/>

  <LogoutDialog></LogoutDialog>

  <ToastNotification></ToastNotification>
</template>

<style>
</style>

<script>
import ToastNotification from './components/ToastNotification.vue';
import LogoutDialog from './components/LogoutDialog.vue';

export default {

  components: {
    ToastNotification,
    LogoutDialog,
  }

}

</script>