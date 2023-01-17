#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (error, data) => {
  console.log(error || data);
});
