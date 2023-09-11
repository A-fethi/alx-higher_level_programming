#!/usr/bin/node
const square = process.argv[2];
let i = 0;
if (process.argv.length > 2 && !isNaN(parseInt(process.argv[2]))) {
  while (i < square) {
    let j = 0;
    let row = '';
    while (j < square) {
      row = row + 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
