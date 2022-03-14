<template>
    <div class="flex justify-center mt-10">
        <div class=" sm:w-3/4 md:w-1/2 flex flex-col items-center rounded-lg shadow-2xl mb-20">
            <h3 class=" text-m-orange-500 text-4xl my-6 font-bold">Nouvelle Recette</h3>
            <Form class="flex flex-col items-center w-full">
                <label class="mb-1" for="name">Nom de la recette</label>
                <Field id="name"
                    v-model="recipe.name" 
                    type="text" 
                    name="name"
                    class=" border-2
                        mb-4
                        pl-2
                        rounded
                        border-m-orange-500 " />

                <label class="mb-1" for="difficulty">Difficulté</label>
                <Field id="difficulty"
                    v-model="recipe.difficulty" 
                    type="number" 
                    name="difficulty"
                    class="hidden" />
                <StarRating class="mb-4 pl-2" @onRatingChange="(n) => recipe.difficulty = n"></StarRating>
                <label class="mb-1" for="time">Temps</label>
                <Field id="time"
                    v-model="recipe.time" 
                    type="time" 
                    name="time"
                    class=" border-2
                        mb-4
                        pl-2
                        rounded
                        border-m-orange-500 " />

                <div class="border border-m-orange-500 w-3/4 mt-4"></div>
                <h2 class=" text-m-orange-500 text-2xl my-4 font-semibold">Ingrédients</h2>

                <IngredientContainer></IngredientContainer>

            </Form>
        </div>
    </div>

</template>


<script>
import { Form, Field, ErrorMessage } from 'vee-validate';
import StarRating from './StarRating.vue'; 
import IngredientContainer from './IngredientContainer.vue';

export default {
    components: {
        Form,
        Field,
        ErrorMessage,
        StarRating,
        IngredientContainer
    },
    data() {
        return {
            ingredientCount: 0,
            recipe: {
                name: '',
                difficulty: 0,
                time: '',
                ingredients: [{
                    name: '',
                    quantity: 0,
                    unity: ''
                }],
                steps: [],
            },
            ingredients: [],
        }
    },
    methods: {
        addIngredient() {
            this.recipe.ingredients.push({
                name: '',
                quantity: 0,
                unity: ''
            });
        },
    },


}

</script>