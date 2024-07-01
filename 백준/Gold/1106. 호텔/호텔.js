const fs = require('fs'); 
const input = fs.readFileSync('/dev/stdin').toString().trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));
const [C, N] = input.shift();

const dp = new Array(C + 1).fill(Infinity);
dp[0] = 0;

for (let [cost, people] of input) {
  if (dp[people] > cost) dp[people] = cost;
  for (let i = 1; i <= C; i++) {
    dp[i] =
      i < people
        ? Math.min(dp[i], cost)
        : Math.min(dp[i], dp[people] + dp[i - people]);
  }
}

console.log(dp[C]);