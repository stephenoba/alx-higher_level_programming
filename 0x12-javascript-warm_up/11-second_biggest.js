#!/usr/bin/node

const args = process.argv;
let numbers = args.slice(2);

const convElements = (ele) => {
  let res = Number(ele);
  if (!res) {
    res = 0;
  }
  return res;
};

if (args.length > 2) {
  numbers = numbers.map(convElements);
  numbers.sort((a, b) => b - a);
  console.log(Number(numbers[1]));
} else {
  console.log(0);
}
