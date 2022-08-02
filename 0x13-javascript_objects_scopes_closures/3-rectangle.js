#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) &&
        h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
