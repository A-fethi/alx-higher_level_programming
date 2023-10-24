#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
const options = { json: true };

req(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const completedtasks = {};
    for (const task of body) {
      if (task.completed) {
        if (completedtasks[task.userId]) {
          completedtasks[task.userId] += 1;
        } else {
          completedtasks[task.userId] = 1;
        }
      }
    }
    console.log(completedtasks);
  }
});
