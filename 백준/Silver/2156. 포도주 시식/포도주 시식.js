const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const solution = (n, w) => {
  if (n == 1) {
    return w[0];
  } else if (n == 2) {
    return w[0] + w[1];
  } else {
    let ans = Array.from({ length: n }, () => 0);
    ans[0] = w[0];
    ans[1] = w[0] + w[1];
    ans[2] = Math.max(ans[1], w[0] + w[2], w[1] + w[2]);

    for (let i = 3; i < n; i++) {
      ans[i] = Math.max(
        ans[i - 3] + w[i - 1] + w[i],
        w[i] + ans[i - 2],
        ans[i - 1]
      );
    }

    return Math.max(...ans)
  }
};

const n = Number(input[0]); // 포도주 잔의 개수
let w = Array.from({ length: n }, () => 0);
for (let i = 1; i <= n; i++) {
  w[i - 1] = Number(input[i].trim());
}
if (n == 0) {
  console.log(0)
  
} else {
  
  console.log(solution(n, w))
}
