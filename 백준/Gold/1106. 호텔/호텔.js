const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [c, n] = input[0].split(" ").map(Number); // 늘려야 하는 고객 c, 홍보할 수 있는 도시 n
let dp = Array(c + 1).fill(Infinity); // 도시당 비용 100보다 작거나 같은 자연수 ; 드는 비용
dp[0] = 0;

for (let i = 1; i <= n; i++) {
  const [a, b] = input[i].split(" ").map(Number); // 비용 a, 증가하는 고객의 수 b
  if (dp[b] > a) dp[b] = a;
  for (let j = 1; j <= c; j++) {
    dp[j] = j < b ? Math.min(dp[j], a) : Math.min(dp[j], dp[b] + dp[j - b]);
  }
}

console.log(dp[c]);
