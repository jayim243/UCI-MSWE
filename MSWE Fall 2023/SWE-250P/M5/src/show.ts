// show recipe button module

export const showRecipes = (recipes: string[]) => {
    return () => { // needs to return something when invoked
        alert(recipes);
    };
};