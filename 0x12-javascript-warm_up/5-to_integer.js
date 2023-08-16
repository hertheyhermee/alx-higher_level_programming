#!/usr/bin/node
<<<<<<< HEAD

const [, , arg] = process.argv;

const checkInt = parseInt(arg);
// isNaN is means is not a number
// parseInt converts the argument to an integer
if (!isNaN(checkInt)) {
  console.log(`My number: ${checkInt}`);
} else {
  console.log('Not a number');
}
=======
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
>>>>>>> 72e9be9576e5039860a084e7c6d0f46e2872563e
