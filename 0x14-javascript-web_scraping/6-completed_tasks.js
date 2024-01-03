#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const tasksCompletedByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (tasksCompletedByUser[todo.userId]) {
        tasksCompletedByUser[todo.userId]++;
      } else {
        tasksCompletedByUser[todo.userId] = 1;
      }
    }
  }

  console.log(tasksCompletedByUser);
});
