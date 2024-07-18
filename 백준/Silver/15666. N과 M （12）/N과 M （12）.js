const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = (depth) => {
  if (depth == m) {
    const tmpStr = tmp.join(" ");
    if (!unique.has(tmpStr)) {
      unique.add(tmpStr);
      ans.push(tmp.join(' '));
    }
    return;
  }

  for (let i = 0; i < n; i++) {
    if (depth == 0 || tmp[depth - 1] <= arr[i]) {
      tmp.push(arr[i]);
      f(depth + 1);
      tmp.pop();
    }
  }
};

const [n, m] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);
let tmp = [];
let ans = [];
let unique = new Set();
f(0);
ans.map((a, _) => {
  console.log(a)
})
