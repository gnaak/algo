const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = () => {
  let min = 1;
  let max = c[n - 1];

  while (min <= max) {
    let mid = Math.floor((min + max) / 2);

    let cnt = c.reduce((a, c) => a + Math.floor(c / mid), 0);

    if (cnt >= m) min = mid + 1;
    else max = mid - 1;
  }
    console.log(max)
};

const [m, n] = input[0].split(" ").map(Number); // m은 조카의 수, n은 과자의 수
const c = input[1].split(" ").map(Number);
c.sort((a, b) => a - b);
f(m, n, c);
