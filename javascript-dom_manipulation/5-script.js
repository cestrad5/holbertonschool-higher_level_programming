// Add a click event to the element with ID "update_header"
document.getElementById("update_header").addEventListener("click", updateText);

// Function to update the text content of the header element
function updateText() {
    // Select the header element and set its text content to "New Header!!!"
    document.querySelector("header").textContent = "New Header!!!";
}
