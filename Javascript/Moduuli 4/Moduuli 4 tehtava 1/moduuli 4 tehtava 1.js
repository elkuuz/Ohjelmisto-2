// Add an event listener to the form
document.getElementById('searchForm').addEventListener('submit', async function (event) {
  event.preventDefault(); // Prevent form submission and page refresh

  const query = document.getElementById('query').value.trim();
  if (!query) {
    alert("Please enter a TV series name.");
    return;
  }

  const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;
  const resultsContainer = document.getElementById('results');
  resultsContainer.innerHTML = ''; // Clear old results

  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();

    if (data.length === 0) {
      resultsContainer.innerHTML = '<p>No results found.</p>';
      return;
    }

    data.forEach(tvShow => {
      // Create an article element for each TV show
      const article = document.createElement('article');

      // Create and append the name (h2 element)
      const name = document.createElement('h2');
      name.textContent = tvShow.show.name;
      article.appendChild(name);

      // Create and append the link (a element)
      const link = document.createElement('a');
      link.href = tvShow.show.url;
      link.textContent = "View Details";
      link.target = "_blank"; // Open in a new tab
      article.appendChild(link);

      // Determine the image URL using a ternary operator
      const imageUrl = tvShow.show.image
        ? tvShow.show.image.medium
        : "https://via.placeholder.com/210x295?text=Not%20Found";

      // Create and append the image (img element)
      const img = document.createElement('img');
      img.src = imageUrl;
      img.alt = tvShow.show.name;
      article.appendChild(img);

      // Create and append the summary (div element)
      const summary = document.createElement('div');
      summary.innerHTML = tvShow.show.summary || "No summary available.";
      article.appendChild(summary);

      // Append the article to the results container
      resultsContainer.appendChild(article);
    });
  } catch (error) {
    console.error("Error fetching data:", error.message);
    resultsContainer.innerHTML = '<p>Something went wrong. Please try again later.</p>';
  }
});
