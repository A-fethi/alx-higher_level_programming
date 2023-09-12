#!/usr/bin/node
const Squareinherit = require('./5-square');
class Square extends Squareinherit {
  charPrint (c) {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let row = '';
      while (j < this.width) {
        if (c === undefined) {
          row = row + 'X';
        } else {
          row = row + 'C';
        }
        j++;
      }
      console.log(row);
      i++;
    }
  }
}
module.exports = Square;
