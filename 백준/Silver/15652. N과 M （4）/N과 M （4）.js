const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [a, b] = input[0].split(" ").map(Number);
const arr = Array.from({ length: a }, (_, i) => i + 1);
const tmp = Array.from({ length: b }, () => 0);

const f = (num, depth) => {
  if (depth === b) {
    console.log(tmp.join(' '));
    return;
  }

  for (let k of arr) {
    tmp[depth] = k;
    if (depth === 0 || tmp[depth] >= tmp[depth - 1]) {
      f(num, depth + 1);
    }
    tmp[depth] = 0;
  }
};

f(a, 0);
