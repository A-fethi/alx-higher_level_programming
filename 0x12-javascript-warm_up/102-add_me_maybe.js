#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let i = 0;
  while (++i < number) {
    i++;
  }
  theFunction(i);
};
