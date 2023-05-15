Array.prototype.last = function () {
  if (this.length === 0) {
    return -1;
  } else {
    return this[this.length - 1];
  }
};

// Test cases
const nums1 = [1, 2, 3];
console.log(nums1.last());

const nums2 = [];
console.log(nums2.last());
