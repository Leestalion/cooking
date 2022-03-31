<template>
    <div class="flex flex-wrap gap-10 m-10 justify-center">
        <div v-for="recipe in recipes" class="w-64 h-40 border-m-orange-500 rounded border-2 flex flex-col items-center">
            <h1 class=" font-bold text-m-orange-500 text-xl">{{ recipe.name }}</h1>
            <p>temps : {{ recipe.time }}</p>
            <p>difficultée : {{ recipe.difficulty }}</p>
            <p>utilisateur : {{ recipe.user_id }}</p>
        </div>
    </div>
</template>


<script>

import { useRecipeStore } from "../store/recipes"


export default {
    setup() {
        const recipeStore = useRecipeStore();

        return { recipeStore };
    },

    data() {
        return {
            recipes: null,
        }
    },

    async created() {
        const [error, data] = await this.recipeStore.fetchRecipes();

        if (error != null) {
            console.log(error);
        } else {
            this.recipes = data;
        }
    }
}

</script>