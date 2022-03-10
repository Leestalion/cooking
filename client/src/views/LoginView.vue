<script setup>
import HeaderVue from '../components/Header.vue';
import LoginVue from '../components/Login.vue';
import router from '../router';
import { useLoggedInUserStore } from '../store/loggedInUser';

const loggedInUserStore = useLoggedInUserStore();
</script>

<template>
    <div>
        <HeaderVue></HeaderVue>
        <div class="flex justify-center">
            <LoginVue></LoginVue>
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