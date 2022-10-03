#!/usr/bin/node
const args = parseInt(process.argv[2], 10);
function factorial(n) {
   if(isNaN(n) || n === 0) {
        return 1;
   } else {
        return (n*factorial(n-1));
   }
}
console.log(factorial(args));
