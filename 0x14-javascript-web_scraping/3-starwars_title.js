#!/usr/bin/nodejs
/* 
- Prints the title of a Star Wars movie where
  the episode number matches a given integer.
*/
const request = require('request');
const info = {
  url: `http://swapi.co/api/films/${process.argv[2]}/`,
  method: 'GET'
};
request(info, function (error, response, body) => {
  try {
  console.log(JSON.parse(body).title);
  } catch (error) {
    throw (error);
  }
});
