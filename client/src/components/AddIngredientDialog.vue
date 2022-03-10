<template>
    <div class="bg-m-grey-500 bg-opacity-70 absolute top-0 left-0 w-full h-full backdrop-blur-sm flex justify-center items-center" v-if="showAddIngredientPopup">
        <div class=" bg-white rounded shadow-md flex flex-col items-center p-5">
            <h3 class="text-2xl text-m-orange-500 font-bold">Ajouter un ingrédient</h3>

            <input type="text" placeholder="Rechercher un ingrédient..." v-model="search" v-on:keydown.enter.prevent
                class="border-2
                    my-4
                    pl-2
                    w-3/4
                    rounded
                    border-m-orange-500 ">

            <div class="grid md:grid-cols-4 grid-cols-2 gap-4 bg-m-grey-300 m-5 rounded shadow-md p-3 max-h-72 max-w-lg overflow-x-hidden grow-0" ref="grid">
                <div v-for="(ingredient, i) in filteredList"
                    @click="ingredientClicked(ingredient)"
                    :ref="ingredient.name"
                    class="w-24 h-16 bg-m-grey-100 rounded cursor-pointer text-m-orange-500 hover:scale-105 transition-transform duration-1000 flex flex-col items-center justify-center"
                    :class="{'col-span-2 h-40 w-52 md:w-[27rem] md:col-span-4 hover:scale-100 cursor-default': ingredient.chosen}">
                    <p class=" font-semibold text-center">{{ ingredient.name }}</p>
                    <span v-if="ingredient.chosen" class="flex justify-center items-center"><input type="number" placeholder="Quantité" class="border-2
                        my-4
                        mr-3
                        pl-2
                        w-1/2
                        rounded
                        border-m-orange-500 "> unité</span>
                        <svg v-if="ingredient.chosen" xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 cursor-pointer self-end mr-6 hover:scale-110 transition-transform" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                        </svg>
                </div>
            </div>

            <div class="flex-col-reverse sm:flex-row flex items-center justify-end p-4 rounded-b-md">
                <button type="button" class="btn-secondary" @click="$emit('hideAddIngredientPopup')">Annuler</button>
                <button @click.prevent class="btn-primary ml-1 mb-3 sm:mb-0">Confirmer</button>
            </div>
        </div>
    </div>

    
</template>


<script>

export default {
    props: [
        'showAddIngredientPopup',
    ],
    data() {
        return {
            chosenIngredient: null,
            ingredientList: [
                {name: 'Carotte', chosen: false},
                {name: 'Pomme de terre', chose: false},
                {name: 'Yaourt', chosen: false},
                {name: 'Tomate', chosen: false},
                {name: 'Poireau', chosen: false},
                {name: 'Pomme', chosen: false},
                {name: 'Poire', chosen: false},
                {name: 'Citron', chosen: false},
                {name: 'Lait', chosen: false},
                {name: "Huile d'olive", chosen: false},
                {name: 'Sucre', chosen: false},
                {name: 'Sel', chosen: false},
                {name: 'Poivre', chosen: false},
                {name: 'Champignons', chosen: false},
                {name: 'Clémentine', chosen: false},
                {name: 'Pain de mie', chosen: false},
                {name: 'Avocat', chosen: false},
                {name: 'Beurre', chosen: false},
                {name: 'Basilic', chosen: false},
                {name: 'Oignon', chosen: false},
                {name: 'Ail', chosen: false},
                {name: 'Pate', chosen: false},
                {name: 'Riz', chosen: false},
            ],
            search: '',
        }
    },

    computed: {
        filteredList() {
            return this.ingredientList.filter(ingredient => {
                return ingredient.name.toLowerCase().includes(this.search.toLowerCase())
            })
        }
    },

    methods: {
        ingredientClicked(ingredient) {
            if(this.chosenIngredient) {
                this.chosenIngredient.chosen = false;
            }
            ingredient.chosen = true;
            this.chosenIngredient = ingredient;

            var grid = this.$refs['grid'];
            var [element] = this.$refs[this.chosenIngredient.name];
            grid.scrollTop = element.offsetTop - grid.clientHeight - 100;

            if(element.offsetTop > 700 ) {
                grid.scrollTop = grid.scrollHeight - grid.clientHeight;
                console.log(grid.scrollTop);
            }
        }
    }
}

</script>