#!/usr/bin/nodejs
// function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  for (let i = 0; list[i]; i++) {
    let container = 0;
    if (list[i] === searchElement) {
      container += 1;
    }
  }
  return (container);
};
