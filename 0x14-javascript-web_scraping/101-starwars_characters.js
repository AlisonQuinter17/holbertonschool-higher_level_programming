#!/usr/bin/node
// Prints all characters of a Star Wars movie:
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  else {
    let t = 0;
    for (t of JSON.parse(body).characters) {
      request(t, 'utf8', (error, response, body) => {
        if (error) throw error;
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
