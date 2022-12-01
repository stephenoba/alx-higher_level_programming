#!/usr/bin/node

class Square extends require('./5-square') {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c)
    {
      for (let i = 0; i < this.height; i++) {
	console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
