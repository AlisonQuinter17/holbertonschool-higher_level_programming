#!/usr/bin/nodejs
// Print the rectangle.
module.exports = class rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    while (this.height) {
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }
};
