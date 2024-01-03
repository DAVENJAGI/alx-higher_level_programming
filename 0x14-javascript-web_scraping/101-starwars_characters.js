#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
const requestUrl = `${url}/${id}`;
// const characterUrl = 'https://swapi-api.alx-tools.com/api/films/`${id}`/characters/people';

request(requestUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with code:', response.statusCode);
  } else {
    const data = JSON.parse(body);
    const filmCharacter = data.characters;
    const order = [];
    let characterFetched = 0;

    filmCharacter.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          character.push(character.name);
	  characterFetched++;
	  if (characterFetched === characterUrl.length) {
            character.forEach(name => console.log(name));
          } else {
            console.error('Error getting character:', error);
          }
        }
      });
    });
  }
});
