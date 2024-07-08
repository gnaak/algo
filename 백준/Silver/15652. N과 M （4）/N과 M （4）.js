const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = (depth) => {
  if (depth == m) {
    output += tmp.join(" ");
    output += "\n";
    return;
  } else {
    for (let i = 1; i <= n; i++) {
      if (depth == 0 || tmp[depth - 1] <= i) {
        tmp.push(i);
        f(depth + 1);
        tmp.pop();
      }
    }
  }
};

const [n, m] = input[0].split(" ");
let output = "";
let tmp = [];
f(0);
console.log(output);
