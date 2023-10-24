#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const options = { json: true };

req(`https://swapi-api.alx-tools.com/api/films/${id}`, options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    for (const chars of body.characters) {
      req(chars, options, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
