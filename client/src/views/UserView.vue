<template>
  <Header></Header>
  <AddRecipeButton></AddRecipeButton>
  <User></User>
</template>

<script>
import Header from '../components/Header.vue';
import AddRecipeButton from '../components/AddRecipeButton.vue';
import User from '../components/User.vue';

export default {
  components: {
    Header,
    AddRecipeButton,
    User
}
}

</script>