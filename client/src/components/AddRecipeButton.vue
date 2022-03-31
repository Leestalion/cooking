<template>
    <div class="flex justify-center my-5">
        <button class="btn-primary text-2xl" @click="goToAddRecipe">Ajouter une recette</button>
    </div>
</template>


<script>
import router from "../router"

export default {
    methods: {
        goToAddRecipe() {
            router.push({name: 'addRecipe'});
        }
    }
}
</script>