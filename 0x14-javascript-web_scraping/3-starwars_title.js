#!/usr/bin/node
// makes get request for SW movie id
const request = require('request');
request(`https://swapi.co/api/films/${process.argv[2]}`, function (error, response, body) {
  error && console.log(error);
  console.log(JSON.parse(body).title);
});
