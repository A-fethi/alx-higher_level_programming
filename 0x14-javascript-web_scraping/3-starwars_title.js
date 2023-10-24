#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const options = { json: true };

req(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
