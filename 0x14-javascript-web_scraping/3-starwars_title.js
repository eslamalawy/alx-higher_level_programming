#!/usr/bin/node
// Using the StarWars API to get movie titles

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
