#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('No argument');
} else {
  for (const arg of args.slice(2)) {
    console.log(arg);
  }
}
