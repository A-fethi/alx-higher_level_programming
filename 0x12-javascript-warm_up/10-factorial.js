#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const result = factorial(parseInt(process.argv[2]));
console.log(result);
