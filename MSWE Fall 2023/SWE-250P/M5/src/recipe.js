// Recipe interface/class module
// recipe class with optional ingredients parameters for now
export class Recipe {
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
