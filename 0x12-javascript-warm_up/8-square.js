#!/usr/bin/node
const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
if (num) {
  let i; let side = '';
  for (i = 0; i < num; i++) {
    side += 'X';
  }
  for (i = 0; i < num; i++) {
    console.log(side);
  }
} else {
  console.log('Missing size');
}
