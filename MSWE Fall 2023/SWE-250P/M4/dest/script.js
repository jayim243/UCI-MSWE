"use strict";
document.addEventListener('DOMContentLoaded', function () {
    let count = 0; // number of recipes submitted by users
    const display = document.getElementById("recipe-count-display");
    const input = document.getElementById("new-recipe-input");
    const submit = document.getElementById("submit-recipe-button");
    let recipes = []; // recipes submitted stored in an array 
    const show = document.getElementById("recipes-submitted");
    // recipe class with optional ingredients parameters for now
    class Recipe {
        constructor(name, ingredients) {
            this.name = name;
            this.ingredients = ingredients;
        }
        displayRecipe() {
            var _a;
            console.log(`Recipe: ${this.name}`);
            console.log(`Ingredients: ${(_a = this.ingredients) === null || _a === void 0 ? void 0 : _a.join(', ')}`);
        }
    }
    // arrow function that happens when user clicks submit button
    const addRecipe = () => {
        ++count;
        display.textContent = "Number of Requested Recipes Submitted!: " + count;
        const recipe = new Recipe(input.value); // creating new Recipe obj
        recipes.push(recipe.name); // adding recipe to list of recipes shown when button is pressed
        recipe.displayRecipe(); // calling Recipe method to log 
        input.value = "";
    };
    submit.addEventListener("click", addRecipe);
    const showRecipes = () => {
        alert(recipes);
    };
    show.addEventListener("click", showRecipes);
});
