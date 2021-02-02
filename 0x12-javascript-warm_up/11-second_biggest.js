#!/usr/bin/node
// The second biggest number.

const array = process.argv.slice(2).sort();

if (array.length <= 1) {
  console.log('0');
} else {
  const len = array.length;
  console.log(array[len - 2]);
}
