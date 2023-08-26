#!/usr/bin/node

const [, , arg] = process.argv;

const checkInt = parseInt(arg);
// isNaN is means is not a number
// parseInt converts the argument to an integer
if (!isNaN(checkInt)) {
  console.log(`My number: ${checkInt}`);
} else {
  console.log('Not a number');
}
