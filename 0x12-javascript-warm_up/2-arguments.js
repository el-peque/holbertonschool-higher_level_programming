#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs[0]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
