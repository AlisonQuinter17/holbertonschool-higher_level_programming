#!/usr/bin/nodejs
/* 
- Prints the title of a Star Wars movie where
  the episode number matches a given integer.
*/
const request = require('request');
const info = {
  url: `https://swapi.co/api/films/${process.argv[2]}/`,
  method: 'GET'
};
request(info, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
