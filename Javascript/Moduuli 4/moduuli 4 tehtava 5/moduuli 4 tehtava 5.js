// Function to fetch and display a random Chuck Norris joke
async function getChuckNorrisJoke() {
  const apiUrl = "https://api.chucknorris.io/jokes/random";

  try {
    const response = await fetch(apiUrl); // Fetch data from the API

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json(); // Parse JSON response

    console.log("Random Chuck Norris Joke:");
    console.log(data.value); // Print only the joke
  } catch (error) {
    console.error("Error fetching joke:", error.message);
  }
}

// Call the function to get and display the joke
getChuckNorrisJoke();
