const unity = [
    { text: 'unité', value: 0 },
    { text: 'g', value: 1 },
    { text: 'mL', value: 2 },
    { text: 'tasse (c)', value: 3 },
    { text: 'cuillère à soupe (Tbs)', value: 4 },
    { text: 'cuillère à café (tsp)', value: 5 },
]

class Ingredient extends Object{
    constructor(id, name, unity, quantity = null, clicked = false, selected = false) {
        super();
        this.id = id;
        this.name = name;
        this.unity = unity;
        this.quantity = quantity;
        this.clicked = clicked;
        this.selected = selected;
    }
}

class Ingredients extends Array {
    constructor(ingredientList, receivedFromBackend = false) {
        super();
        if(ingredientList !== 0 && ingredientList != null) {

            // in case received from backend
            if (receivedFromBackend) {
                ingredientList.forEach((element, index) => {
                    this[index] = new Ingredient(element.ingredient_id, element.ingredient_name, element.unity);
                });
            } else {
                if (!(ingredientList instanceof Ingredients) && ingredientList instanceof Array) {
                    ingredientList.forEach((element, index) => {
                        this[index] = new Ingredient(element.id, element.name, element.unity, element.quantity, element.clicked, element.selected);
                    });
                } else if (!(ingredientList instanceof Ingredients)) {
                    console.log("wrong type given to new Ingredient(), received : ");
                    console.log(ingredientList);
                    return;
                }
            }


            this.mSort();
        }
    }

    newIngredient(name, unity) {
        this.players.push(new Ingredient(name, unity));
    }

    get allIngredients() {
        return this.ingredients
    }

    mFilter(callback) {
        return this.filter(callback);
    }

    mEntries() {
        return this.entries();
    }

    mIndexOf(ingredient) {
        return this.indexOf(ingredient);
    }

    mSort() {
        var list = this.sort(function(first, second) {
            if( second.selected && !first.selected) {
                return 1;
            } else if ( !second.selected && first.selected) {
                return -1;
            } else {
                var textA = first.name.toUpperCase();
                var textB = second.name.toUpperCase();
                return (textA < textB) ? -1 : (textA > textB) ? 1 : 0
            }
        });

        return new Ingredient(list);
    }

    containsIngredient(ingredient) {
        var found = false;
        this.forEach((mIngredient) => {
            if (mIngredient.id === ingredient.id) {
                found = true;
                return;
            }
        });
        return found;
    }

    containsIngredientIndex(ingredient) {
        var found = false;
        var mIndex = -1;
        this.forEach((mIngredient, index) => {
            if (mIngredient.id === ingredient.id) {
                found = true;
                mIndex = index;
                return;
            }
        });
        return [found, mIndex];
    }

    getIngredientFromId(id) {
        var found = false;
        this.forEach((mIngredient) => {
            if (mIngredient.id === id) {
                found = mIngredient;
                return;
            }
        });
        return found;
    }

    mSplice(index, count) {
        return this.splice(index, count);
    }

    removeIngredient(mIngredient) {
        var tmp = new Ingredients();
        var index = 0
        if (this.containsIngredient(mIngredient)) {
            this.forEach((ingredient) => {
                if (ingredient.id != mIngredient.id) {
                    tmp[index] = ingredient;
                    index ++;
                }
            });
        }
        
        return tmp;

    }

    static get unity() {
        return unity;
    }
}

export { Ingredients, Ingredient }