#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  if (list && searchElement) {
    for (const ele of list) {
      if (ele === searchElement) {
        count++;
      }
    }
  }
  return count;
};
