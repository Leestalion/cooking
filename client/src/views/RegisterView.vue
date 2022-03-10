<script setup>
import HeaderVue from '../components/Header.vue';
import router from '../router';
import { useLoggedInUserStore } from '../store/loggedInUser';
import RegisterVue from '../components/Register.vue';

const loggedInUserStore = useLoggedInUserStore();
</script>

<template>
    <div>
        <HeaderVue></HeaderVue>
        <div class="flex justify-center">
            <RegisterVue></RegisterVue>
        </div>
    </div>
</template>


<script>

export default {
    created() {
        // if (this.loggedInUserStore.getIsLoggedIn) {
        //     this.goToHome();
        // }
    },
    methods: {
        goToHome() {
            router.push({name: 'home'});
        }
    }
}
</script>