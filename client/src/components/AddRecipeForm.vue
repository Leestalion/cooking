<template>
    <div class="flex justify-center mt-10">
        <div class="sm:w-3/4 md:w-1/2 flex flex-col items-center rounded-lg shadow-2xl mb-20">
            <h3 class="text-m-orange-500 text-4xl my-6 font-bold">Nouvelle Recette</h3>
            <Form class="flex flex-col items-center w-full" :validation-schema="schema" @submit="handleAddRecipe">
                <span class="flex items-center">
                    <Field
                        @keydown.enter.prevent
                        id="name"
                        placeholder="Nom de la recette"
                        v-model="recipe.name"
                        type="text"
                        name="name"
                        class="box-border mb-4 pl-2 rounded outline-none border-2 border-m-grey-100 bg-m-grey-100 focus:bg-white focus:border-m-orange-500 transition-all"
                    />
                </span>
                <ErrorMessage name="name" class="text-m-orange-500 text-sm"/>

                <label class="mb-1" for="difficulty">Difficulté</label>
                <Field
                    id="difficulty"
                    v-model="recipe.difficulty"
                    type="number"
                    name="difficulty"
                    class="hidden"
                />
                <StarRating class="mb-4 pl-2" ref="StarRatingComponent" @onRatingChange="(n) => recipe.difficulty = n"></StarRating>
                <label class="mb-1" for="time">Temps</label>
                <Field
                    @keydown.enter.prevent
                    id="time"
                    v-model="recipe.time"
                    type="time"
                    name="time"
                    class="box-border mb-4 pl-2 rounded outline-none border-2 border-m-grey-100 bg-m-grey-100 focus:bg-white focus:border-m-orange-500 transition-all"
                />
                <ErrorMessage name="time" class="text-m-orange-500 text-sm"/>

                <div class="border border-m-orange-500 w-3/4 mt-4"></div>
                <h2 class="text-m-orange-500 text-2xl my-4 font-semibold">Ingrédients</h2>

                <IngredientContainer ref="ingredientContainerComponent"></IngredientContainer>

                <div class="border border-m-orange-500 w-3/4 mt-4"></div>
                <h2 class="text-m-orange-500 text-2xl my-4 font-semibold">Etapes</h2>

                <div v-for="(step, index) in recipe.steps" :key="step.id" class="flex gap-3 w-full justify-center">
                    <div>
                        <div class="bg-m-orange-500 rounded-full h-10 w-10 text-white flex items-center justify-center font-bold text-xl mb-2">
                            {{ index + 1 }}
                        </div>
                        <div class="bg-m-orange-500 rounded-full h-8 w-8 text-white flex items-center justify-center font-bold text-xl cursor-pointer"
                            @click="deleteStep(index)"
                            v-if="recipe.steps.length != 1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="transition-transform h-5 w-5  hover:scale-110 stroke-white" fill="none" viewBox="0 0 24 24" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                            </svg>
                        </div>
                    </div>
                    <textarea
                        type="text"
                        v-model="recipe.steps[index].text"
                        class="w-2/3 h-40 box-border mb-4 pl-2 rounded outline-none border-2 border-m-grey-100 bg-m-grey-100 focus:bg-white focus:border-m-orange-500 transition-all"
                    />
                </div>

                <div
                    class=" w-1/4 h-8 mb-8 bg-m-orange-500 rounded cursor-pointer text-white active:scale-90 hover:scale-110 transition-all duration-100 flex items-center justify-center"
                    @click="addStepField"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-10 w-10"
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

                <div class="border border-m-orange-500 w-3/4 mb-4"></div>

                <input
                    @click="reset"
                    type="reset"
                    class="font-bold w-2/3 h-8 mb-2 rounded cursor-pointer text-m-orange-500 border-m-orange-500 border-2 active:scale-95 hover:scale-105 transition-all duration-100 flex items-center justify-center"
                >

                <input
                    @click.prevent="handleAddRecipe"
                    type="submit"
                    class="font-bold w-2/3 h-8 mb-8 bg-m-orange-500 rounded cursor-pointer text-white active:scale-95 hover:scale-105 transition-all duration-100 flex items-center justify-center"
                >
            
                
            </Form>
        </div>
    </div>
</template>


<script>
import { Form, Field, ErrorMessage } from 'vee-validate';
import StarRating from './StarRating.vue';
import IngredientContainer from './IngredientContainer.vue';
import { useIngredientStore } from '../store/ingredients';
import { useRecipeStore } from '../store/recipes';
import * as yup from 'yup';
import { useToastNotifStore } from '../store/toastNotif';
import router from '../router';

export default {
    setup() {
        const ingredientStore = useIngredientStore();
        const recipeStore = useRecipeStore();
        const toastNotifStore = useToastNotifStore();

        return { ingredientStore, recipeStore, toastNotifStore };
    },
    components: {
        Form,
        Field,
        ErrorMessage,
        StarRating,
        IngredientContainer
    },
    data() {
        const schema = yup.object().shape({
            name: yup.string().required('Il est nécessaire de donner un nom à la recette'),
            time: yup.string().required("Il est nécessaire de donner un temps à la recette")
        });
        return {
            ingredientCount: 0,
            recipe: {
                name: '',
                difficulty: 0,
                time: '',
                steps: [],
                ingredients: [],
            },
            schema,
            ingredients: [],
            counterSteps: 0,
        }
    },
    created() {
        this.addStepField();
    },

    methods: {
        goToHome() {
            router.push({name: 'home'})
        },

        addStepField() {
            this.recipe.steps.push({
                id: this.counterSteps,
                text:""
            });

            this.counterSteps++;
        },

        deleteStep(index) {
            this.recipe.steps.splice(index, 1);
        },

        async handleAddRecipe() {

            this.recipe.ingredients = this.ingredientStore.ingredientsSelected;

            console.log(this.recipe);

            const [error, data] = await this.recipeStore.addRecipe(this.recipe);

            if (error) {
                console.log(error);
            } else {
                this.toastNotifStore.showSnack("La recette a bien été créée");
                this.goToHome();
            }
        },

        reset() {
            this.ingredientStore.emptySelectedIngredients();

            this.$refs.ingredientContainerComponent.emptyIngredients();
            this.$refs.StarRatingComponent.reset();

            this.recipe.steps = [];
            this.addStepField();
        }
    },



}

</script>