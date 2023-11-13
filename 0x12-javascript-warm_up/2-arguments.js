#!/usr/bin/node

const args = process.argv.length;

//check the length of the process
if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
