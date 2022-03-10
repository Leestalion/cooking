import { defineStore } from "pinia";
import { useLocalStorage  } from '@vueuse/core';



const useLogoutDialogStore = defineStore({
    id: 'logoutDialog',
    state: () => ({
        logoutDialog: useLocalStorage('logoutDialog', false),
    }),
    getters: {
        getLogoutDialog: (state) => state.logoutDialog,
    },
    actions: {
       showLogout() {
           this.logoutDialog = true;
       },
       closeLogout() {
           this.logoutDialog = false;
       }
    }
})


export { useLogoutDialogStore };