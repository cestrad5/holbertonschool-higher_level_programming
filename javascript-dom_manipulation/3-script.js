// Add a click event to the element with ID "toggle_header"
document.getElementById("toggle_header").addEventListener("click", toggleColour)

//Function to toggle the header color
function toggleColour() {
  //Selecting the header element
  const header = document.querySelector("header");
  //Using toggle to switch between colors
  header.classList.toggle("red");
  header.classList.toggle("green");
  
}