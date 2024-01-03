#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const file_encoding = 'utf-8';

fs.readFile (filepath, file_encoding, (err, data) => {
	if (err) {
		console.error('Error: ', err);
	} else {
		console.log(data);
	}});
