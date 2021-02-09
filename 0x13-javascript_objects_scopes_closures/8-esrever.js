#!/usr/bin/nodejs
// Returns the reversed version of a list.
exports.esrever = function (list) {
  emptylist = [];
  let i = 0;
  while (list[i]) {
    i++;
  }
  for (j = i; list[j]; j--) {
    emptylist.push(list[j]);
  }
  return (emptylist);
};
