#!/usr/bin/node
const myArgs = process.argv.slice(2);
let maxNum = parseInt(myArgs[0]);
let auxNum = parseInt(myArgs[0]);
let num; let i;

if (myArgs.length < 2) {
  console.log(0);
} else {
  for (i = 0; i < myArgs.length; i++) {
    num = parseInt(myArgs[i]);
    if (num > maxNum) {
      maxNum = num;
    }
    if (num < auxNum) {
      auxNum = num;
    }
  }
  for (i = 0; i < myArgs.length; i++) {
    num = parseInt(myArgs[i]);
    if (num > auxNum && num < maxNum) {
      auxNum = num;
    }
  }
  console.log(auxNum);
}
