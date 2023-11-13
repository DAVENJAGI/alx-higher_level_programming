#!/usr/bin/node

function add (a, b) {
  if (typeof a !== 'number') {
    a = parseInt(a);
  }
  if (typeof b !== 'number') {
    b = parseInt(b);
  }
  return a + b;
}

console.log(add(process.argv[2], process.argv[3])); 
