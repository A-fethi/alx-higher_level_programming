#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let j = 0;
  while (list[i]) {
    if (list[i] === searchElement) {
      j++;
    }
    i++;
  }
  return j;
};
