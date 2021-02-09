#!/usr/bin/node
// makes get request for SW movie id
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
