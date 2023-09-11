#!/usr/bin/node
const x = process.argv[2];
let i = 0;
if (process.argv.length > 2 && !isNaN(parseInt(process.argv[2]))) {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
