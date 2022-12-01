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

  rotate () {
    if (this.width !== this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
