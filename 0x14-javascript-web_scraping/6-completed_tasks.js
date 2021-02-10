#!/usr/bin/nodejs
// Computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  else {
    const d = {};
    let total = 0;
    for (const task of JSON.parse(body)) {
      if (task.completed) d[task.userId] ? d[task.userId]++ : d[task.userId] = 1;
   }
   console.log(d);
  }
});
