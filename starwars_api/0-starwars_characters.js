#!/usr/bin/node
/*
 * This script prints all characters of a Star Wars movie.
 * The movie ID is passed as the first command line argument.
 */

const request = require('request');

// Get the movie ID from the command line.
const movieId = process.argv[2];

// Build the API URL for the selected movie.
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Request the movie data from the Star Wars API.
request(filmUrl, (error, response, body) => {
  if (error) {
    return;
  }

  // Convert the JSON response into a JavaScript object.
  const filmData = JSON.parse(body);

  // Get the list of character URLs from the movie data.
  const characterUrls = filmData.characters;

  /*
   * Print characters one by one.
   * This keeps the same order as the characters list from the API.
   */
  function printCharacter (index) {
    // Stop when all characters have been printed.
    if (index >= characterUrls.length) {
      return;
    }

    // Request the current character data.
    request(characterUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        return;
      }

      // Convert the character JSON response into an object.
      const characterData = JSON.parse(charBody);

      // Print the character name.
      console.log(characterData.name);

      // Move to the next character only after printing the current one.
      printCharacter(index + 1);
    });
  }

  // Start printing from the first character.
  printCharacter(0);
});
