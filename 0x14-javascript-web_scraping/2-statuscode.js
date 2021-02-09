#!/usr/bin/nodejs
// Display the status code of a GET request.
const request = require('request');
const info = {
    url: process.argv[2],
    method: 'GET'
};
request(info, (response) => {
    console.log('code:', response.statusCode);
});
