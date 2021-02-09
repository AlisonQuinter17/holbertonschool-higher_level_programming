#!/usr/bin/nodejs
// defines a square and inherits from Square Class.
const Square = require('./5-square.js');

module.exports = class Square extends Square {
  constructor (size) {
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      const character = 'X';
    } else {
      const character = 'C';
    }
    for (let j = c; j; j--) {
      console.log(character.repeat(c));
    }
  }
};
