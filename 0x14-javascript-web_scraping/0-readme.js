#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const fileEncoding = 'utf-8';

fs.readFile(filepath, fileEncoding, (err, data) => {
  if (err) {
    console.error('Error: ', err);
  } else {
    console.log(data);
  }
});
