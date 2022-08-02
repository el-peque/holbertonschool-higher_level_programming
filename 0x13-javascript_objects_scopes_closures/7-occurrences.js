#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i; let count = 0;
  for (i of list) {
    if (i === searchElement) {
      count++;
    }
  }
  return (count);
};
