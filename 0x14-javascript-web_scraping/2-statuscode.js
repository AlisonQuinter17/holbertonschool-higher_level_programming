#!/usr/bin/nodejs
// Display the status code of a GET request.
const request = require('request');
const info = {
    url: process.argv[2],
    method: 'GET'
};
request(info, () => {
    console.log('code:', request.status);
});
