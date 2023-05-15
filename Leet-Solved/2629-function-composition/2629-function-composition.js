function compose(functions) {
  return function(x) {
    if (functions.length === 0) {
      return x;
    }

    let result = x;
    for (let i = functions.length - 1; i >= 0; i--) {
      result = functions[i](result);
    }

    return result;
  };
}


const functions1 = [
  (x) => x + 1,
  (x) => x * x,
  (x) => 2 * x
];
const fn1 = compose(functions1);
const x1 = 4;
const output1 = fn1(x1);
console.log(output1);


const functions2 = [
  (x) => 10 * x,
  (x) => 10 * x,
  (x) => 10 * x
];
const fn2 = compose(functions2);
const x2 = 1;
const output2 = fn2(x2);
console.log(output2); 


const functions3 = [];
const fn3 = compose(functions3);
const x3 = 42;
const output3 = fn3(x3);
console.log(output3); 
