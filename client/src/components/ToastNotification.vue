<script setup>
import { useToastNotifStore } from '../store/toastNotif';
import { mapState } from 'pinia';
const toastNotifStore = useToastNotifStore();
</script>

<template>
    <transition name="fade">
        <div v-if="localToastNotifVisible" class="p-5 absolute border-4 border-green-500 w-3/4 left-[12.5%] bottom-10 rounded-full text-green-500 font-bold flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p class="pl-2">{{ message }}</p>
        </div>
    </transition>
</template>

<script>


export default {
    computed: {
        ...mapState(useToastNotifStore, {
            localToastNotifVisible: 'snack',
            message: 'message',
        })

    },
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