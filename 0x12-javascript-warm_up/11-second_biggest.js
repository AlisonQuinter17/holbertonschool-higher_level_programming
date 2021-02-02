#!/usr/bin/nodejs
// The second biggest number.

const array = process.argv.slice(2).sort();

if (array.length <= 1) {
  console.log('0');
} else {
  len = array.length;
  console.log(array[len - 2]);
}
