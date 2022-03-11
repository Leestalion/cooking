<script setup>
import { useLoggedInUserStore } from '../store/loggedInUser';

const loggedInUserStore = useLoggedInUserStore();
</script>

<template>
    <div>
        <Header></Header>
        <div class="flex justify-center">
            <Login></Login>
        </div>
    </div>
</template>


<script>

import Header from '../components/Header.vue';
import Login from '../components/Login.vue';
import router from '../router';

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