#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];
const fileEncoding = 'utf-8';

request(url, fileEncoding, (err, response, body) => {
  if (err) {
    console.error('Error: ', err);
  }
  const writeableStream = fs.createWriteStream(filepath);
  writeableStream.write(body);
  writeableStream.end();
});
