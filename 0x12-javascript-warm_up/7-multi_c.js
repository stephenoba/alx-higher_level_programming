#!/usr/bin/node

const args = process.argv;
const number = Number(args[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
