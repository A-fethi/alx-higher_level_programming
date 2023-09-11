#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
}
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
}
