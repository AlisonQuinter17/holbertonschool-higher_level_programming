#!/usr/bin/nodejs
/* 
- Prints the title of a Star Wars movie where
  the episode number matches a given integer.
*/
const request = require('request');

request(`https://swapi.co/api/films/${process.argv[2]}/`, function (error, response, body) {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
