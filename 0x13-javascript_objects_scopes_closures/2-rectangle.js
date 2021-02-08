#!/usr/bin/nodejs
// Creates a class Rectangle that defines a rectangle.
module.exports = 
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  if (w <= 0 || h <= 0) {
    this.width = NaN;
    this.height = NaN;
  }
};