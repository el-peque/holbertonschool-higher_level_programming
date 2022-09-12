#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv[2];
fs.readFile(myArgs, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
