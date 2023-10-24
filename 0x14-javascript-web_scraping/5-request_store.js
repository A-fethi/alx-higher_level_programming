#!/usr/bin/node
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const path = process.argv[3];

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
