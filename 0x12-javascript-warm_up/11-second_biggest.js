#!/usr/bin/node

const args = process.argv;
const numbers = args.slice(2);

if (args.length > 2) {
  numbers.sort().reverse();
  console.log(Number(numbers[1]));
} else {
  console.log(0);
}
