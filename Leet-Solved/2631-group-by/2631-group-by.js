Array.prototype.groupBy = function (fn) {
  return this.reduce((result, item) => {
    const key = fn(item);
    if (!(key in result)) {
      result[key] = [];
    }
    result[key].push(item);
    return result;
  }, {});
};

// Example usage
const array1 = [
  {"id":"1"},
  {"id":"1"},
  {"id":"2"}
];
const fn1 = (item) => item.id;
console.log(array1.groupBy(fn1));

const array2 = [
  [1, 2, 3],
  [1, 3, 5],
  [1, 5, 9]
];
const fn2 = (list) => String(list[0]);
console.log(array2.groupBy(fn2));

const array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const fn3 = (n) => String(n > 5);
console.log(array3.groupBy(fn3));
