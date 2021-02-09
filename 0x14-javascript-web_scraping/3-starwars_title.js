#!/usr/bin/nodejs
/* 
- Prints the title of a Star Wars movie where
  the episode number matches a given integer.
*/
const request = require('request');
const info = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  method: 'GET'
};
request(info, (err, response, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
