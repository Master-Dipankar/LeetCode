function sleep(millis) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(millis);
    }, millis);
  });
}

let t1 = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t1);
});

let t2 = Date.now();
sleep(200).then(() => {
  console.log(Date.now() - t2);
});
