#!/usr/bin/node

<<<<<<< HEAD
const [, , arg1, arg2] = process.argv;

const firstArg = arg1 === undefined ? 'undefined' : arg1;
const secondArg = arg2 === undefined ? 'undefined' : arg2;

console.log(`${firstArg} is ${secondArg}`);
=======
console.log(`${process.argv[2]} is ${process.argv[3]}`
>>>>>>> 72e9be9576e5039860a084e7c6d0f46e2872563e
