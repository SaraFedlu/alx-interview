#!/usr/bin/node
const request = require('request');

// Validate input
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Star Wars API base URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie data from Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Fetch each character and display in the correct order
  printCharactersInOrder(characters, 0);
});

// Recursive function to print characters in order
function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return; // Base case: All characters have been printed
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);
    printCharactersInOrder(characters, index + 1);
  });
}
