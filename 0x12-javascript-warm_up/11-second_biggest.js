#!/usr/bin/node
if (process.argv.length === 2 || process.argv[3] === undefined) {
  console.log('0');
}
if (process.argv.length > 3) {
  const sortedargs = process.argv.slice(2).sort();
  const revsortedargs = sortedargs.reverse();
  console.log(revsortedargs[1]);
}
