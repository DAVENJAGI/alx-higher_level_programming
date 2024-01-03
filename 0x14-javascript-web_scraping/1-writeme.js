#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const string = process.argv[3];
const fileEncoding = 'utf-8';

fs.writeFile(filepath, string, fileEncoding, (err) => {
  if (err) {
    console.error('Error: ', err);
  } else {
    console.log("Done!!");
  }
});
