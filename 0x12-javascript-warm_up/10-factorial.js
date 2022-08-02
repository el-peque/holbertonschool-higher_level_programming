#!/usr/bin/node
const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
console.log(factorial(num));

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}
