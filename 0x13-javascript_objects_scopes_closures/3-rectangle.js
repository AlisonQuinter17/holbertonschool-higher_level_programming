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
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.with; j++) {
        console.log('X');
      }
      console.log('\n');
    }
  }
};
