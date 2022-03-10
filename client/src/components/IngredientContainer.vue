<template>
    <div class="m-3 rounded bg-m-grey-300 grid grid-cols-3">
        
        <div v-for="ingredient in ingredients" class="w-16 h-16 bg-m-grey-100 m-3 rounded cursor-pointer text-m-orange-500 hover:scale-105 transition-all duration-100"></div>

        <div class="w-16 h-16 bg-m-grey-100 m-3 rounded cursor-pointer text-m-orange-500 active:scale-90 hover:scale-105 transition-all duration-100"
            @click="addIngredient">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
        </div>
        
    </div>

    <AddIngredientDialog @hideAddIngredientPopup="hideIngredientPopup" :showAddIngredientPopup="showAddIngredientPopup"></AddIngredientDialog>

</template>

<script>
import AddIngredientDialog from "./AddIngredientDialog.vue";

export default {
    data() {
        return {
            ingredients: [],
            showAddIngredientPopup: false,
        };
    },
    methods: {
        addIngredient() {
            this.showAddIngredientPopup = true;
            document.documentElement.style.overflow = 'hidden';
            // this.ingredients.push({ "ingredient": 0 });
        },
        hideIngredientPopup() {
            this.showAddIngredientPopup = false
                        document.documentElement.style.overflow = 'auto';
        }
    },
    components: { AddIngredientDialog }
}

</script>