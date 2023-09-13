// Define an asynchronous function named getName
async function getName() {
    // Use the Fetch API to make a GET request to the specified URL
    const response = await fetch("https://swapi-api.hbtn.io/api/people/4/?format=json");

    // Parse the response as JSON
    const data = await response.json();

    // Set the text content of the element with id "character" to the retrieved name
    document.getElementById("character").textContent = data.name;
}

// Call the getName function to fetch and display the character name
getName();
