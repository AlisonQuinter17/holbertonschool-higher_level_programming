#!/usr/bin/nodejs
// Returns the reversed version of a list.
exports.esrever = function (list) {
  const reversedlist = [];
  for (j = list.lenght - 1; j >= 0; j--) {
    reversedlist.push(list[j]);
  }
  return (reversedlist);
};
