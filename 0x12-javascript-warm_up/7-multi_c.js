#!/usr/bin/node
const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
if (num) {
  let i;
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
