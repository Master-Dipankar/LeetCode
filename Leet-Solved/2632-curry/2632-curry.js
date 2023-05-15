function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    } else {
      return function (...moreArgs) {
        return curried(...args, ...moreArgs);
      };
    }
  };
}

function sum(a, b, c) {
  return a + b + c;
}

const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3));
console.log(curriedSum(1)(2, 3));  
console.log(curriedSum(1, 2)(3));  
console.log(curriedSum(1, 2, 3));  

function life() {
  return 42;
}

const curriedLife = curry(life);
console.log(curriedLife());  
