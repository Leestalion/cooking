import { defineStore } from "pinia";
import { authService } from "../services/auth.service";
import { useLocalStorage  } from '@vueuse/core';
import IngredientHelper from '../models/ingredients';


const useIngredientStore = defineStore({
    id: 'ingredients',
    state: () => ({
        ingredients: [],
        ingredientsSelected: useLocalStorage("ingredientsSelected", [])
    }),
    getters: {
        getIngredients: (state) => state.ingredients,
        getSelectedIngredients: (state) => state.ingredientsSelected
    },
    actions: {
        async addIngredient(ingredient) {
            try {
                const { data } = await authService.post('/addingredient', ingredient);
                if (data.ingredient) {
                    var newIngredient = IngredientHelper.createIngredient(data.ingredient.ingredient_id, data.ingredient.ingredient_name, data.ingredient.unity);
                    this.ingredients.push(newIngredient)
                    return [null, this.ingredients, newIngredient];
                } else if (data.error) {
                    return [data.error];
                }
            } catch (error) {
                return  [error];
            }
        },

        async fetchIngredients() {
            try {
                const { data } = await authService.get('/ingredients');
                if (data.ingredients) {
                    this.ingredients = data.ingredients;
                    return [null, this.ingredients];
                } else if (data.error) {
                    return [data.error]
                } else {
                    return ["unknown error"];
                }
            } catch (error) {
                return [error];
            }
        },

        setSelectedIngredients(ingredients) {
            this.ingredientsSelected = ingredients;

        },

        removeIngredientsFromSelected(ingredient) {
            IngredientHelper.removeIngredientById(this.ingredientsSelected, ingredient.ingredient_id);
        },

        emptySelectedIngredients() {
            this.ingredientsSelected = [];
        }
    }
})


export { useIngredientStore };