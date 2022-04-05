const unity = [
    { text: 'unité', value: 0 },
    { text: 'g', value: 1 },
    { text: 'mL', value: 2 },
    { text: 'tasse (c)', value: 3 },
    { text: 'cuillère à soupe (Tbs)', value: 4 },
    { text: 'cuillère à café (tsp)', value: 5 },
]

export default {
    removeIngredientById(ingredientList, id) {

        for (var i = 0; i < ingredientList.length; i++) {
            var ingredient = ingredientList[i];

            if (id == ingredient.ingredient_id) {
                
                ingredientList.splice(i, 1);
            }
        }
    },

    createIngredient(ingredient_id, ingredient_name, unity) {
        var ingredient =  {
            id: ingredient_id,
            name: ingredient_name,
            unity: unity,
            clicked: clicked,
            selected: selected,
        }
        return ingredient;
    },

    getIngredientFromId(ingredientList, id) {
        var found = false;
        ingredientList.forEach((ingredient) => {
            if (ingredient.ingredient_id === id) {
                found = ingredient;
                return;
            }
        });
        return found;
    },

    sortByName(first, second) {
        if( second.selected && !first.selected) {
            return 1;
        } else if ( !second.selected && first.selected) {
            return -1;
        } else {
            var textA = first.ingredient_name.toUpperCase();
            var textB = second.ingredient_name.toUpperCase();
            return (textA < textB) ? -1 : (textA > textB) ? 1 : 0
        }
    },

    unity,
}