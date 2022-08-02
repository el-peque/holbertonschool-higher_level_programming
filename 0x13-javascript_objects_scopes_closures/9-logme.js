#!/usr/bin/node
let value = 0;
exports.logMe = function (item) {
  value++;
  console.log(value + ': ' + item);
};
