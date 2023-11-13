#!/usr/bin/node

const n = parseInt(Number(process.argv[2]));

if (isNaN(n)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(n)
  for (let i = 0; i < n; i++) console.log(row);
}
