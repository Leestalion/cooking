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
    components: {
        Login,
        Header,
    },
    methods: {
        goToHome() {
            router.push({name: 'home'});
        }
    }
}
</script>