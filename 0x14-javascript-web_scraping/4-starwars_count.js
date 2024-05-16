#!/usr/bin/node
const request = require('request');

// Wedge Antilles movies count
function countMovies (apiEndpoint) {
  const characterId = 18;
  request.get(apiEndpoint, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      let count = 0;
      for (let i = 0; i < films.length; i++) {
        const characters = films[i].characters;
        for (let j = 0; j < characters.length; j++) {
          if (characters[j].includes(characterId)) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}

const args = process.argv.slice(2);

if (args.length === 1) {
  const apiEndpoint = args[0];
  countMovies(apiEndpoint);
}
