function* fibGenerator() {
  let a = 0;
  let b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}


const gen = fibGenerator();


const callCount = 5;
const fibSequence = [];
for (let i = 0; i < callCount; i++) {
  fibSequence.push(gen.next().value);
}

console.log(fibSequence);
