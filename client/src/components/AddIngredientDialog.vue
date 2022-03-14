<template>
    <transition name="fade">
        <div
            class="bg-m-grey-500 bg-opacity-70 fixed top-0 left-0 w-full h-full backdrop-blur-sm flex justify-center items-center"
            v-if="showAddIngredientPopup"
        >
            <div class="bg-white rounded shadow-md flex flex-col items-center p-5 w-11/12 md:w-1/2">
                <h3 class="text-2xl text-m-orange-500 font-bold">Ajouter un ingrédient</h3>

                <span class="w-3/4 flex items-center h-10 my-4">
                    <input
                        @keyup="refreshSearch"
                        type="text"
                        placeholder="Rechercher un ingrédient..."
                        v-model="search"
                        v-on:keydown.enter.prevent
                        class="pl-2 rounded-l w-3/4 h-full outline-none bg-m-grey-100 focus:bg-white focus:border-2 focus:border-m-orange-500"
                    />
                    <button
                        :disabled="newIngredientAvailable"
                        @click.prevent="newIngredientClicked"
                        class="btn-primary w-1/4 h-full p-0 rounded-l-none"
                    >Nouveau</button>
                </span>

                <div
                    class="flex flex-wrap flex-row justify-center gap-3 w-4/5 md:w-11/12 bg-m-grey-300 m-5 rounded shadow-md py-4 h-72 overflow-x-hidden scrollbar-gutter grow-0"
                    ref="grid"
                >
                    <div
                        v-if="newIngredient"
                        class="col-span-2 h-48 w-52 md:w-[27rem] p-4 md:col-span-4 hover:scale-100 bg-m-grey-100 rounded shadow-md text-m-orange-500 flex flex-col"
                    >
                        <p class="font-semibold text-center text-lg">{{ newIngredientName }}</p>

                        <input
                            type="number"
                            placeholder="Quantité"
                            class="border-2 mt-2 pl-2 w-full md:w-1/2 rounded border-m-orange-500 self-center focus:border-m-orange-600 focus:outline-none"
                        />

                        <span class="relative w-full md:w-1/2 self-center">
                            <select
                                class="appearance-none w-full border-2 my-4 mr-3 pl-2 rounded border-m-orange-500 focus:outline-none focus:border-m-orange-600"
                                v-model="newUnity"
                            >
                                <option v-for="unit in unity" :value="unit.value">{{ unit.text }}</option>
                            </select>
                            <div
                                class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
                            >
                                <svg
                                    class="fill-current h-4 w-4"
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 20 20"
                                >
                                    <path
                                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                                    />
                                </svg>
                            </div>
                        </span>
                        <span class="self-end md:mr-6 flex">
                            <svg
                                @click="leave"
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-10 w-10 cursor-pointer hover:scale-110 transition-dimension"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                                stroke-width="2"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    d="M6 18L18 6M6 6l12 12"
                                />
                            </svg>
                            <svg
                                @click="AddNewIngredient"
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-10 w-10 cursor-pointer hover:scale-110 transition-dimension"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                    clip-rule="evenodd"
                                />
                            </svg>
                        </span>
                    </div>

                    <div
                        v-else
                        v-for="(ingredient, i) in filteredList"
                        @click="ingredientClicked(ingredient)"
                        :ref="ingredient.name"
                        :class="[ingredient.clicked ? 'hover:scale-100 cursor-default w-10/12 h-40 transition-dimension ' :
                        'cursor-pointer hover:scale-105 w-48 h-14 transition-transform ',
                        'text-m-orange-500 bg-m-grey-100 flex flex-col items-center justify-center rounded shadow-md p-2 relative']"
                    >
                        <p class="font-semibold text-center">{{ ingredient.name }}</p>

                        <span v-if="ingredient.selected && !ingredient.clicked" class="flex">
                            <p>{{ ingredient.quantity }}</p>
                            <p  v-if="unity[ingredient.unity]" class="ml-1">{{ unity[ingredient.unity].text }}</p>
                        </span>

                        <span v-if="ingredient.selected && !ingredient.clicked" class="absolute top-2 left-2" @click.stop="deleteIngredient(ingredient)">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                            </svg>
                        </span>

                        <span v-if="ingredient.clicked" class="flex justify-center items-center w-full md:w-1/2">
                            <input
                                v-model="ingredient.quantity"
                                type="number"
                                placeholder="Quantité"
                                class="border-2 mt-2 pl-2 rounded border-m-orange-500 self-center focus:border-m-orange-600 focus:outline-none w-full"
                            />
                        </span>
                        <span v-if="ingredient.clicked" class="relative w-full md:w-1/2 self-center">
                            <select
                                class="appearance-none w-full border-2 my-4 mr-3 pl-2 rounded border-m-orange-500 focus:outline-none focus:border-m-orange-600"
                                v-model="ingredient.unity"
                            >
                                <option v-for="unit in unity" :value="unit.value">{{ unit.text }}</option>
                            </select>
                            <div
                                class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
                            >
                                <svg
                                    class="fill-current h-4 w-4"
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 20 20"
                                >
                                    <path
                                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                                    />
                                </svg>
                            </div>
                        </span>


                        <svg
                            v-if="ingredient.clicked"
                            @click.stop="selectIngredient(ingredient)"
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-5 w-5 md:h-10 md:w-10 cursor-pointer self-end hover:scale-110 transition-dimension absolute right-2 bottom-2"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                clip-rule="evenodd"
                            />
                        </svg>
                    </div>

                    <div
                        v-if="noIngredients"
                        class="font-semibold h-20 w-full text-m-orange-500 bg-m-grey-100 flex flex-col items-center justify-center rounded shadow-md transition-dimension text-center p-2"
                    >Aucun ingrédient trouvé, créez en un nouveau !</div>
                </div>

                <div
                    class="flex-col-reverse sm:flex-row flex items-center justify-end p-4 rounded-b-md"
                >
                    <button
                        type="button"
                        class="btn-secondary"
                        @click="$emit('hideAddIngredientPopup')"
                    >Annuler</button>
                    <button @click.prevent="confirmButtonClicked" class="btn-primary ml-1 mb-3 sm:mb-0">Confirmer</button>
                </div>
            </div>
        </div>
    </transition>
</template>


<script>

import { useIngredientStore } from '../store/ingredients';
import { Ingredients } from '../models/ingredients';

export default {
    props: [
        'showAddIngredientPopup',
    ],
    setup() {
        const ingredientStore = useIngredientStore();

        return { ingredientStore };
    },
    emits: [
        'confirm',
        'hideAddIngredientPopup'
    ],
    data() {
        return {
            chosenIngredient: null,
            newIngredient: false,
            newIngredientName: '',
            newUnity: 0,
            ingredientList: new Ingredients(),
            search: '',
            unity: [],
        }
    },

    async created() {

        if (this.ingredientStore.getIngredients == null || this.ingredientStore.getIngredients.length === 0) {
            const [error, ingredients] = await this.ingredientStore.fetchIngredients();
            if (error) {
                console.log(error);
            }
            this.ingredientList = this.setSelectedParameter(ingredients);

        } else {
            this.ingredientList = this.ingredientStore.getIngredients;
        }

        this.ingredientList.mSort();

        this.unity = Ingredients.unity;

    },

    computed: {
        filteredList() {
            if (this.ingredientList != null) {
                return this.ingredientList.mFilter((ingredient) => {
                    if (ingredient.name) {
                        return ingredient.name.toLowerCase().includes(this.search.toLowerCase());
                    } else {
                        return false;
                    }

                });
            } else {
                return false;
            }


        },

        noIngredients() {
            return (this.filteredList.length <= 0) && !this.newIngredient
        },

        newIngredientAvailable() {
            var present = false;

            if (this.search == "") {
                return true;
            }

            for (const [index, ingredient] of this.ingredientList.mEntries()) {
                present = present || ingredient.name === this.search;
            }
            return present;
        },
    },

    methods: {
        ingredientClicked(ingredient) {

            if (this.chosenIngredient || ingredient.selected) {
                this.chosenIngredient.clicked = false;
            }
            ingredient.clicked = true;
            this.chosenIngredient = ingredient;

            var grid = this.$refs['grid'];
            var [element] = this.$refs[this.chosenIngredient.name];

            if (!ingredient.clicked) {
                grid.scrollTop = element.offsetTop - grid.clientHeight;

                if (element.offsetTop > 700) {
                    grid.scrollTop = grid.scrollHeight - grid.clientHeight;
                }
            }

        },

        newIngredientClicked() {
            this.newIngredient = true;
            this.newIngredientName = this.search;
        },
        leave() {
            this.newIngredient = false;
        },

        refreshSearch() {
            if (this.newIngredient) {
                this.newIngredient = false;
            }

            if (this.chosenIngredient) {
                this.chosenIngredient.clicked = false;
            }
        },

        async AddNewIngredient() {
            var ingredient = {
                'ingredient_name': this.newIngredientName,
                'unity': this.newUnity
            };

            const [error, ingredients] = await this.ingredientStore.addIngredient(ingredient);

            if (error) {
                console.log(error);
            } else {
                this.ingredientList = ingredients;
                this.newIngredient = false;

                this.selectIngredient(ingredient)
            }
        },

        selectIngredient(ingredient) {

            if (ingredient == this.chosenIngredient) {

                if (ingredient.quantity) {
                    ingredient.selected = true;

                    this.ingredientList.forEach(ingredient => {
                        ingredient.clicked = false;
                    });

                    this.ingredientList.mSort();
                } else {
                    console.log("veuillez fournir une quantité");
                }
            } else {
                console.log("les ingrédients ne correspondent pas");
            }
        },

        confirmButtonClicked() {

            this.ingredientStore.setSelectedIngredients(this.filterSelectedIngredients(this.ingredientList));
            this.$emit('confirm');
        },

        deleteIngredient(ingredient) {
            ingredient.selected = false;
            ingredient.quantity = null;
            ingredient.unity = 0;
            // this.ingredientStore.removeIngredientsFromSelected(ingredient);
            this.ingredientList.mSort();
        },

        filterSelectedIngredients(ingredients) {
            return ingredients.mFilter((ingredient) => {
                return (ingredient.selected == true);
            });
        },

        setSelectedParameter(ingredients) {

            var selectedIngredients = this.ingredientStore.getSelectedIngredients

            ingredients.forEach((ingredient) => {
                
                var selectedIngredient = selectedIngredients.getIngredientFromId(ingredient.id)

                if (selectedIngredient) {
                    
                    ingredient.selected = selectedIngredient.selected;
                    ingredient.quantity = selectedIngredient.quantity;
                    ingredient.unity = selectedIngredient.quantity;
                    
                }
            })
            return ingredients;
        },
    }
}

</script>