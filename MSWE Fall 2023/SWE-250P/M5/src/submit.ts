// submit button module

import { Recipe } from "./recipe.js";

let count: number = 0;

export const addRecipe = (display: HTMLElement, input: HTMLInputElement, recipes: string[]) => {
    ++count;
    display.textContent = "Number of Requested Recipes Submitted!: " + count;
    console.log(count)
    const recipe = new Recipe(input.value);
    recipes.push(recipe.name);

    recipe.displayRecipe();
    input.value = "";
};
