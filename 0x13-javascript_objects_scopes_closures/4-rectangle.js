#!/usr/bin/nodejs
// Print, rotate and multiplies the rectangle.
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (; this.height; this.height--) {
        console.log('X'.repeat(this.width));
      }
    }
    rotate () {
      const temp = this.width;
      this.width = this.height;
      this.width = temp;
    }
    double() {
      this.width *= 2;
      this.height *= 2;
    }
  };
  