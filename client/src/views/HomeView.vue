<template>
  <Header></Header>
  <AddRecipeButton></AddRecipeButton>
  <Recipes></Recipes>
</template>

<script>
import Header from '../components/Header.vue';
import AddRecipeButton from '../components/AddRecipeButton.vue';
import Recipes from '../components/Recipes.vue';

export default {
  components: {
    Header,
    AddRecipeButton,
    Recipes
}
}

</script>