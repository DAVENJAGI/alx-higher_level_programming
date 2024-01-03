#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;
// const requestUrl = `${url}/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body).results;

    let count = 0;
    for (const film in data) {
      const characters = data[film].characters;
      for (const film in characters) {
        if (characters[film].includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
