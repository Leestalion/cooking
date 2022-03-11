<script setup>
import { useLoggedInUserStore } from '../store/loggedInUser';
const loggedInUserStore = useLoggedInUserStore();
</script>

<template>
    <div>
        <Header></Header>
        <div class="flex justify-center">
            <Register></Register>
        </div>
    </div>
</template>


<script>

import Register from '../components/Register.vue';
import Header from '../components/Header.vue';
import router from '../router';


export default {
    components: {
        Register,
        Header,
    },
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