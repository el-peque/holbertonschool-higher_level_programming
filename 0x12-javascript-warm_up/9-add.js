#!/usr/bin/node
const myArgs = process.argv.slice(2);
const firstNum = parseInt(myArgs[0]);
const secondNum = parseInt(myArgs[1]);
console.log(add(firstNum, secondNum));
function add (a, b) {
  return (a + b);
}
