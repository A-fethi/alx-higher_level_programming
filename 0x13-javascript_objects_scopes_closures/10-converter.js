#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (num) {
    return num.toString(base);
  }
  return myConverter;
};
