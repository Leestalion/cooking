import { defineStore } from "pinia";
import { authService, baseService } from "../services/auth.service";
import { useLocalStorage  } from '@vueuse/core';

const NOT_LOGGED_ERROR = 100;
const ERROR_RECIPE_ALREADY_EXIST = 603;


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
                if (data.recipe) {
                    return [null, data.recipe];
                } else if (data.error) {
                    if (data.error == ERROR_RECIPE_ALREADY_EXIST) {
                        return ["Une recette porte déjà le même nom !"]
                    } else if (data.error == NOT_LOGGED_ERROR) {
                        return ["Erreur de connexion à la session de l'utilisateur"]
                    } else {
                        return [data.error];
                    }

                }
            } catch (error) {
                console.log(error);
                return  [error];

            }
        },


        async fetchRecipes() {
            try {
                const { data } = await baseService.post('/recipes');
                if (data.recipes) {
                    return [null, data.recipes];
                } else if (data.error) {
                    return [data.error];
                } else {
                    return ["unknown error"];
                }
            } catch (error) {
                return [error];
            }
        },

        async getCurrentUserRecipes() {
            try {
                const { data } = await authService.post('/current-user-recipes');
                if (data.recipes) {
                    return [null, data.recipes];
                } else if (data.error) {
                    return [data.error];
                } else {
                    return ["unknown error"];
                }
            } catch (error) {
                return [error];
            }
        },

        async deleteRecipe(id) {
            try {
                const { data } = await authService.post('/delete-recipe', {'id': id});
                return [null, data];
            } catch (error) {
                return [error];
            }
        }
    }
})


export { useRecipeStore };