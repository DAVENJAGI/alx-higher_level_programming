#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, response, body => {
  if (err) {
    console.error('code: ', response.statusCode);
  } else {
	  console.log('code: ', response.statusCode);
  }
});
