// Recipe interface/class module

export interface Recipe {
    name: string;
    ingredients?: string[];
}

// recipe class with optional ingredients parameters for now
export class Recipe implements Recipe {
    constructor(name: string, ingredients?: string[]) {
        this.name = name;
        this.ingredients = ingredients;
    }

    displayRecipe(): void { // Recipe class method to log recipe and ingredients
        console.log(`Recipe: ${this.name}`);
        console.log(`Ingredients: ${this.ingredients?.join(', ')}`);
    }
}