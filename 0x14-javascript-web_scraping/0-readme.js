#!/usr/bin/nodejs
// Reads and prints the content of a file in utf-8.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(err ? err : data);
});
