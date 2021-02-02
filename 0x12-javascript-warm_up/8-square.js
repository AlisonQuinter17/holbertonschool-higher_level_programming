#!/usr/bin/node
// prints a square.

const size = process.argv[2];

if (!size) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    for (let s = 0; s < j; s++) {
      console.log('X');
    }
  }
}
