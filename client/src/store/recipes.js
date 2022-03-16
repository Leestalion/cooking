import { defineStore } from "pinia";
import { authService } from "../services/auth.service";
import { useLocalStorage  } from '@vueuse/core';


const useRecipeStore = defineStore({
    id: 'recipes',
    state: () => ({
        recipe: useLocalStorage("recipe", null),
    }),
    getters: {
        getRecipe: (state) => new Ingredients(state.recipe),
    },
    actions: {
        async addRecipe(recipe) {
            try {
                const { data } = await authService.post('/addrecipe', recipe);
                if (data.error) {
                    return [data.error];
                }
            } catch (error) {
                return  [error];
            }
        },
    }
})


export { useIngredientStore };