#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

const firstArg = arg1 === undefined ? 'undefined' : arg1;
const secondArg = arg2 === undefined ? 'undefined' : arg2;

console.log(`${firstArg} is ${secondArg}`);
