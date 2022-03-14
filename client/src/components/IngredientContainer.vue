<template>
    <div class="m-3 rounded bg-m-grey-300 grid grid-cols-3">
        <div
            v-for="ingredient in ingredients"
            class="w-16 h-16 bg-m-grey-100 m-3 rounded cursor-pointer text-m-orange-500 hover:scale-105 transition-all duration-100"
        >
            <p>{{ ingredient.name }}</p>
            <span class=" flex">
                <p>{{ ingredient.quantity }}</p>
                <p v-if="unity[ingredient.unity]" class="ml-1">{{ unity[ingredient.unity].text }}</p> <!-- very weird comportement of javascript, telling undefined when var is defined -->
            </span>
        </div>

        <div
            class="w-16 h-16 bg-m-grey-100 m-3 rounded cursor-pointer text-m-orange-500 active:scale-90 hover:scale-105 transition-all duration-100"
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
        ref="open"
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
    },
    components: { AddIngredientDialog }
}

</script>