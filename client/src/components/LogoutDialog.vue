<script setup>
import { useLogoutDialogStore } from '../store/dialogs';
import { mapState } from 'pinia';
const logoutDialogStore = useLogoutDialogStore();
</script>

<template>
  <transition name="fade">
    <div class="bg-m-grey-500 bg-opacity-70 absolute top-0 left-0 w-full h-full backdrop-blur-sm flex justify-center items-center" v-if="showLogout">
      <div
        class="bg-m-grey-500 text-white rounded-md transition-all w-2/3 md:w-1/2 "
        id="logoutModal"
        tabindex="-1"
      >
        <div
          class="border-none shadow-lg relative flex flex-col w-full pointer-events-auto rounded-md"
        >
          <h5 class="text-xl font-medium p-4" id="logoutModalLabel">Déconnexion</h5>
          <div class="relative p-4">Voulez vous vraiment vous déconnecter ?</div>
          <div class="flex-col-reverse sm:flex-row flex items-center justify-end p-4 rounded-b-md">
            <button type="button" class="btn-secondary" @click="closeLogout">Annuler</button>
            <button @click="logOut" class="btn-primary ml-1 mb-3 sm:mb-0">Déconnexion</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
    computed: {
        ...mapState(useLogoutDialogStore, {
            showLogout: 'logoutDialog',
        })

    },
    methods: {
      closeLogout() {
        this.logoutDialogStore.closeLogout();
      }
    }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>