// Define an asynchronous function named sayHello
async function sayHello() {
  // Use the Fetch API to make a GET request to the specified URL
  const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");

  // Parse the response as JSON
  const data = await response.json();

  // Set the text content of the element with id "hello" to the fetched translation
  document.getElementById("hello").textContent = data.hello;
}

// Call the sayHello function to fetch and display the translation
sayHello();
