import { addRecipe } from "./submit.js"; //MAKE SURE TO INCLUDE .JS BECAUSE JS WON'T KNOW
import { showRecipes } from "./show.js";

document.addEventListener('DOMContentLoaded', function() {
    
    const display = document.getElementById("recipe-count-display") as HTMLElement;
    const input = document.getElementById("new-recipe-input") as HTMLInputElement;
    const recipes: string[] = [];

    const show = document.getElementById("recipes-submitted") as HTMLButtonElement;
    show.addEventListener("click", showRecipes(recipes));

    const submit = document.getElementById("submit-recipe-button") as HTMLButtonElement;
    submit.addEventListener("click", () => addRecipe(display, input, recipes));
});
