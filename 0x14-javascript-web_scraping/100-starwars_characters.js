#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
const requestUrl = `${url}/${id}`;
// const characterUrl = 'https://swapi-api.alx-tools.com/api/films/`${id}`/characters/people';

request(requestUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
