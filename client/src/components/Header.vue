<template>
    <main>
        <div class="bg-m-grey-500 text-white">
            <div
                class="px-5 py-5 grid justify-items-center items-center md:grid-cols-5 xl:grid-cols-7"
            >
                <img
                    @click="goToHome"
                    src="@/assets/logo_simple_white.png"
                    class="object-contain col-span-1 w-[10em]"
                />
                <h1
                    class="text-5xl sm:text-7xl lg:text-9xl font-title md:col-span-3 xl:col-span-5"
                >FAMILY RECIPES</h1>
            </div>
            <div class="flex justify-end mr-5">
                <a href v-if="this.loggedInUserStore.getIsLoggedIn">
                    <button
                        class="text-white font-bold py-2 px-4 border-r border-b-4 border-m-grey-700 hover:border-m-grey-600 hover:bg-m-grey-400 rounded-tl-lg"
                    >{{ this.loggedInUserStore.getUserName }}</button>
                </a>
                <button
                    v-if="this.loggedInUserStore.getIsLoggedIn"
                    class="text-white font-bold py-2 px-4 border-b-4 border-m-grey-700 hover:bg-m-grey-400 hover:border-m-grey-600 rounded-tr-lg transition duration-150 ease-in-out"
                    @click="showLogout"
                >Déconnexion</button>
                <button
                    @click="goToRegister"
                    v-if="!this.loggedInUserStore.getIsLoggedIn"
                    class="text-white font-bold py-2 px-4 border-b-4 border-m-grey-700 hover:border-m-grey-600 hover:bg-m-grey-400 rounded-tl-lg"
                >Inscription</button>
                <button
                    @click="goToLogin"
                    v-if="!this.loggedInUserStore.getIsLoggedIn"
                    class="text-white font-bold py-2 px-4 border-b-4 border-m-grey-700 hover:border-m-grey-600 hover:bg-m-grey-400 rounded-tr-lg"
                >Connexion</button>
            </div>
        </div>

        
    </main>
</template>


<script>
import router from '../router';
import { useLoggedInUserStore } from '../store/loggedInUser';
import { useLogoutDialogStore } from '../store/dialogs';

export default {
    setup() {
        const loggedInUserStore = useLoggedInUserStore();
        const logoutDialogStore = useLogoutDialogStore();

        return {logoutDialogStore, loggedInUserStore}
    },
    methods: {
        async logOut() {
            const [error] = await this.loggedInUserStore.logOut();
            if (error) {
                console.log(error);
            } else {
                this.logoutDialogStore.closeLogout();
                this.goToLogin();
            }
        },

        goToLogin() {
            router.push({ name: 'login' });
        },
        goToHome() {
            router.push({name: 'home'});
        }, 
        goToRegister() {
            router.push({name: 'register'});
        },

        showLogout() {
            this.logoutDialogStore.showLogout();
        }
    },
}
</script>