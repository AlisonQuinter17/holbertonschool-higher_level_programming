#!/usr/bin/node
// Create a sentence concat.

if (process.argv[3]) {
  sentence = process.argv[2].concat(' is ', process.argv[3]);
} else if (process.argv[2]) {
  sentence = process.argv[2].concat(' is undefined');
} else {
  sentence = 'undefined is undefined';
}
console.log(sentence);
