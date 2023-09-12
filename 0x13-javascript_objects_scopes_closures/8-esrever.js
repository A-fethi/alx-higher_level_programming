#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let i = list.length - 1;
  while (i >= 0) {
    reversed[list.length - 1 - i] = list[i];
    i--;
  }
  return reversed;
};
