<template>
    <div class="m-3 rounded bg-m-grey-300 flex flex-wrap flex-row gap-3 justify-center py-4">
        <div
            v-for="ingredient in ingredients"
            class="text-m-orange-500 bg-m-grey-100 flex flex-col items-center justify-center rounded shadow-md p-2 relative w-48 h-14 transition-transform"
        >
            <p class="font-semibold">{{ ingredient.name }}</p>
            <span class=" flex">
                <p>{{ ingredient.quantity }}</p>
                <p v-if="unity[ingredient.unity]" class="ml-1">{{ unity[ingredient.unity].text }}</p> <!-- very weird comportement of javascript, telling undefined when var is defined -->
            </span>

            <div
                class="absolute top-1 left-0 flex items-center px-2 cursor-pointer "
                @click="deleteIngredient(ingredient)"
            >
                <svg xmlns="http://www.w3.org/2000/svg" class="transition-transform h-6 w-6 stroke-m-orange-500 hover:scale-110 text-m-orange-500" fill="none" viewBox="0 0 24 24" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>

            </div>
        </div>

        <div
            class=" w-48 h-14 bg-m-grey-100 rounded cursor-pointer text-m-orange-500 active:scale-90 hover:scale-105 transition-all duration-100 flex items-center justify-center"
            @click="addIngredient"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-16 w-16"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                />
            </svg>
        </div>

    </div>

    <AddIngredientDialog
        @confirm="refreshIngredients"
        @hideAddIngredientPopup="hideIngredientPopup"
        :showAddIngredientPopup="showAddIngredientPopup"
        ref="ingredientPopup"
    ></AddIngredientDialog>
</template>

<script>
import AddIngredientDialog from "./AddIngredientDialog.vue";
import { Ingredients } from "../models/ingredients";
import { useIngredientStore } from "../store/ingredients";

export default {
    setup() {
        const ingredientStore = useIngredientStore();

        return { ingredientStore };
    },
    components: {
        AddIngredientDialog,
    },
    data() {
        return {
            ingredients: new Ingredients(),
            showAddIngredientPopup: false,
            unity: [],
        };
    },
    async created() {

        this.ingredients = this.ingredientStore.getSelectedIngredients;

        this.unity = Ingredients.unity;

    },
    methods: {
        addIngredient() {
            this.showAddIngredientPopup = true;
            document.documentElement.style.overflow = 'hidden';
        },
        hideIngredientPopup() {
            this.showAddIngredientPopup = false;
            document.documentElement.style.overflow = 'auto';
        },
        
        async refreshIngredients() {

            this.ingredients = this.ingredientStore.getSelectedIngredients;

            this.hideIngredientPopup();
        },

        deleteIngredient(ingredient) {

            this.ingredientStore.removeIngredientsFromSelected(ingredient);
            this.ingredients = this.ingredientStore.getSelectedIngredients;

            this.$refs.ingredientPopup.deleteIngredientById(ingredient.id);
        }
    },
    components: { AddIngredientDialog }
}

</script>