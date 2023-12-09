import { addRecipe } from "./submit.js"; //MAKE SURE TO INCLUDE .JS BECAUSE JS WON'T KNOW
import { showRecipes } from "./show.js";
document.addEventListener('DOMContentLoaded', function () {
    const display = document.getElementById("recipe-count-display");
    const input = document.getElementById("new-recipe-input");
    const recipes = [];
    const show = document.getElementById("recipes-submitted");
    show.addEventListener("click", showRecipes(recipes));
    const submit = document.getElementById("submit-recipe-button");
    submit.addEventListener("click", () => addRecipe(display, input, recipes));
});
