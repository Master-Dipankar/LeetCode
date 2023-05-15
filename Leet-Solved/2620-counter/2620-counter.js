function createCounter(n) {
  let count = n;

  return function () {
    const result = count;
    count++;
    return result;
  };
}

const n = 10;
const operations = ["call", "call", "call"];
const counter = createCounter(n);
const output = operations.map(() => counter());
console.log(output);
