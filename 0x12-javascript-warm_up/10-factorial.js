#!/usr/bin/node

const args = process.argv;

function fact (num) {
  let res = 1;

  if (num) {
    for (let i = 1; i <= num; i++) {
      res *= i;
    }
  }
  return res;
}

const number = Number(args[2]);
console.log(fact(number));
