// Add a click event to the element with ID "add_item"
document.getElementById("add_item").addEventListener("click", addToLi)

//Function to add a new item to the list
function addToLi() {
    //create a new element <li>
    const newListItem = document.createElement("li")
    //Set the content new element
    newListItem.textContent = "Item"
    //Selecting my_list class
    const myList = document.querySelector(".my_list");
    //Add the new item to the end of the list
    myList.appendChild(newListItem);
}