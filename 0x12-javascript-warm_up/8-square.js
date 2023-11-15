#!/usr/bin/node

const size = parseInt(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size);
  for (let i = 0; i < size; i++) console.log(row);
}
