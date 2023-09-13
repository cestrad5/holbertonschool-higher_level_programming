// Define an asynchronous function named getMovies
async function getMovies() {
  // Use the Fetch API to make a GET request to the specified URL
  const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");

  // Parse the response as JSON
  const data = await response.json();

  // Get a reference to the ul element with id "list_movies"
  let myMovieList = document.getElementById("list_movies");

  // Loop through the movie objects in the data.results array
  for (const movie of data.results) {
    // Create a new li element
    let newListItem = document.createElement("li");

    // Set the text content of the li element to the movie title
    newListItem.textContent = movie.title;

    // Append the li element to the ul element
    myMovieList.appendChild(newListItem);
  }
}

// Call the getMovies function to fetch and list the movie titles
getMovies();
