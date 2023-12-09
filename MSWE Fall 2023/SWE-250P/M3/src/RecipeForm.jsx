import React, { useState } from 'react';

export default function RecipeForm({ setRecipeCount }) {
  const [newRecipe, setNewRecipe] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Update the recipe count using the setRecipeCount function from props
    setRecipeCount((prevCount) => prevCount + 1);
    console.log('Submitted Recipe:', newRecipe);

    setNewRecipe('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <p>Enter recipe ideas: </p>
      <input
        type="text"
        name="recipeideas"
        value={newRecipe}
        onChange={(e) => setNewRecipe(e.target.value)}
      />
      <input type="submit" name="submit" value="Submit" />
    </form>
  );
}
