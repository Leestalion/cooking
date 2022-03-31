<template>
    <div class="flex flex-wrap gap-10 m-10 justify-center">
        <div v-for="recipe in recipes" class="w-64 h-40 border-m-orange-500 rounded border-2 flex flex-col items-center relative">
            <h1 class=" font-bold text-m-orange-500 text-xl">{{ recipe.name }}</h1>
            <p>temps : {{ recipe.time }}</p>
            <p>difficultée : {{ recipe.difficulty }}</p>
            <p>utilisateur : {{ recipe.user_id }}</p>

            <span 
                @click.stop="showDeleteRecipeDialog(recipe.recipe_id)"
                class="absolute top-2 left-2 text-m-orange-500 cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
            </span>

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
        await this.fetchRecipes();
    },

    methods: {
        async fetchRecipes() {
            const [error, data] = await this.recipeStore.getCurrentUserRecipes();

            if (error != null) {
                console.log(error);
            } else {
                this.recipes = data;
            }
        },

        async showDeleteRecipeDialog(recipeId) {
            await this.recipeStore.deleteRecipe(recipeId);

            await this.fetchRecipes();
        }
    }


}

</script>