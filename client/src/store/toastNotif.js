import { defineStore } from "pinia";
import { useLocalStorage  } from '@vueuse/core';



const useToastNotifStore = defineStore({
    id: 'toastNotif',
    state: () => ({
        snack: useLocalStorage('snack', false),
        message: useLocalStorage('message', ''),
    }),
    getters: {
        getSnack: (state) => state.snack,
    },
    actions: {
       showSnack(message) {
           this.snack = true;
           this.message = message;
           setTimeout(() => {
               this.snack = false;
               this.message = "";
            }, 5000);
       },
    }
})


export { useToastNotifStore };