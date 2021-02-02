#!/usr/bin/nodejs
// Factorial.

function factorial (n) {
  let total = 1;
  let i = 1;
  while (i < n) {
    total *= i;
    i++;
  }
  return total;
}

console.log(factorial(parseInt(process.argv[2])));
