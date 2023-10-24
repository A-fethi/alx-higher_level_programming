#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const id = '/people/18/';

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const count = body.split(id).length - 1;
    console.log(count);
  }
});
