#!/usr/bin/node

const args = process.argv;
const number = Number(args[2]);

if (number) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
