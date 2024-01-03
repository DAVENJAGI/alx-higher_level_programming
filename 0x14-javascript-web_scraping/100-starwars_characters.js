#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
const requestUrl = `${url}/${id}`;
const characterUrl = 'https://swapi-api.alx-tools.com/api/people';

request(requestUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with code:', response.statusCode);
  } else {
//    const data = JSON.parse(body);
    
    request(characterUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body);
//    data.forEach(character) => {
    console.log(characters["name"]);
    }    
    });
  }
});
