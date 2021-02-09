#!/usr/bin/nodejs
// Returns the reversed version of a list.
exports.esrever = function (list) {
  let i = 0;
  while (list[i]) {
    i++;
  }
  for (j = i; list[j]; j--) {
    console.log(list[j]);
  }
};
