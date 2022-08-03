#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
const fileA = fs.readFileSync(myArgs[0], 'utf8');
const fileB = fs.readFileSync(myArgs[1], 'utf8');
fs.appendFile(myArgs[2], fileA + fileB, function (err) {
  if (err) throw err;
});
