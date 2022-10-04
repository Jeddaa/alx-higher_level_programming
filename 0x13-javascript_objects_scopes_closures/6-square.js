#!/usr/bin/node

const FirstSquare = require('./5-square');
module.exports = class Square extends FirstSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
