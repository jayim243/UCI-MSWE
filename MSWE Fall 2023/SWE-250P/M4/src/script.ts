document.addEventListener('DOMContentLoaded', function() {
    let count: number = 0; // number of recipes submitted by users
    const display = document.getElementById("recipe-count-display") as HTMLElement;
    const input = document.getElementById("new-recipe-input") as HTMLInputElement;
    const submit = document.getElementById("submit-recipe-button") as HTMLButtonElement;
    let recipes: String[] = []; // recipes submitted stored in an array 
    const show = document.getElementById("recipes-submitted") as HTMLButtonElement;


    interface Recipe {
        name: String;
        ingredients?: String[];
    }
    
    // recipe class with optional ingredients parameters for now
    class Recipe implements Recipe {
        constructor(name: String, ingredients?: String[]) {
            this.name = name;
            this.ingredients = ingredients;
        }
    
        displayRecipe(): void { // Recipe class method to log recipe and ingredients
            console.log(`Recipe: ${this.name}`);
            console.log(`Ingredients: ${this.ingredients?.join(', ')}`);
        }
    }

    
    // arrow function that happens when user clicks submit button
    const addRecipe = () => { //
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
    }
    show.addEventListener("click", showRecipes);

});
