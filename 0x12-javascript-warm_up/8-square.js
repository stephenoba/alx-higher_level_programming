#!/usr/bin/node

const args = process.argv;
const number = Number(args[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    let x = '';
    for (let j = 0; j < number; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
