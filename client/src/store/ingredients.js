import { defineStore } from "pinia";
import { authService } from "../services/auth.service";
import { Ingredients, Ingredient } from '../models/ingredients';
import { useLocalStorage  } from '@vueuse/core';


const useIngredientStore = defineStore({
    id: 'ingredients',
    state: () => ({
        ingredients: new Ingredients(),
        ingredientsSelected: useLocalStorage("ingredientsSelected", new Ingredients())
    }),
    getters: {
        getIngredients: (state) => new Ingredients(state.ingredients),
        getSelectedIngredients: (state) => new Ingredients(state.ingredientsSelected)
    },
    actions: {
        async addIngredient(ingredient) {
            try {
                const { data } = await authService.post('/addingredient', ingredient);
                if (data.ingredient) {
                    var newIngredient = new Ingredient(data.ingredient.ingredient_id, data.ingredient.ingredient_name, data.ingredient.unity)
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
                    this.ingredients = new Ingredients(data.ingredients, true);
                    return [null, this.ingredients];
                } else if (data.error) {
                    return [data.error]
                }
            } catch (error) {
                return [error];
            }
        },

        setSelectedIngredients(ingredients) {
            if (ingredients instanceof Ingredients) {
                this.ingredientsSelected = ingredients;
            } else {
                this.ingredientsSelected = new Ingredients(ingredients);
            }

        },

        removeIngredientsFromSelected(ingredient) {
            this.ingredientsSelected.pop(this.ingredientsSelected.mIndexOf(ingredient));
        }
    }
})


export { useIngredientStore };