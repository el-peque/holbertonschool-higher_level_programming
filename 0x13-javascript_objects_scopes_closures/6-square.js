#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i; let x = 'X';
    if (c) {
      x = c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
};
