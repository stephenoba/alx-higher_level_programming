#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const numOne = Number(args[2]);
const numTwo = Number(args[3]);
add(numOne, numTwo);
