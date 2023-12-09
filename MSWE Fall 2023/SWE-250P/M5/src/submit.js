// submit button module
import { Recipe } from "./recipe.js";
let count = 0;
export const addRecipe = (display, input, recipes) => {
    ++count;
    display.textContent = "Number of Requested Recipes Submitted!: " + count;
    console.log(count);
    const recipe = new Recipe(input.value);
    recipes.push(recipe.name);
    recipe.displayRecipe();
    input.value = "";
};
