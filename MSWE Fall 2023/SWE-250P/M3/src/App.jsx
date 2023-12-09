import React, { useState } from 'react';
import ReactDOM from 'react-dom'
import Header from './Header';
import Recipes from './Recipes'; 
import RecipeForm from './RecipeForm';
import './style.css'; 


ReactDOM.createRoot(document.getElementById('root')).render(
    <App />
)
// ReactDOM.render(<App />, document.getElementById('root')) //also works


export default function App() {
  const [recipeCount, setRecipeCount] = useState(0);

  return (
    <>
      <Header />
      <p>Welcome to my budget-friendly recipes. All my recipes use eggs, so if you are allergic, then do not proceed.</p>

      <Recipes recipeCount={recipeCount} setRecipeCount={setRecipeCount} />
      <p>Number of Requested Recipes Submitted!: {recipeCount}</p>

      <p>Feel free to request any recipes you'd like to see</p>

      <RecipeForm setRecipeCount={setRecipeCount} />
    </> 
  );
}