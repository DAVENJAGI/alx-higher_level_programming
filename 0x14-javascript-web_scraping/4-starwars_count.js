#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = process.argv[3]
const requestUrl = `${url}/${id}`;

request(requestUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with code:', response.statusCode);
    return;
  }
    const data = JSON.parse(body);
    
//    for (const movie of data.results) {
//    if (movie.characters.includes(id)
//	    movie++;
    
    console.log(data.characters("18"));
//  }
});
