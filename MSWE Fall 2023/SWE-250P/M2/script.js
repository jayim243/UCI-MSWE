// script.js

// Plain JavaScript code to manage state
let recipeCount = 0;

// Function to update the display
function updateDisplay() {
    document.getElementById('recipe-count-display').textContent = `Number of Requested Recipes Submitted!: ${recipeCount}`;
}

// Function to handle button click
function handleButtonClick() {
    recipeCount += 1;
    updateDisplay();

    // Clear the input field
    document.getElementById('new-recipe-input').value = '';
}

// Attach the click event listener
document.getElementById('submit-recipe-button').addEventListener('click', handleButtonClick);

// Initial display update
updateDisplay();
