#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const bit = 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(bit.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
