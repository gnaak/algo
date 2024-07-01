const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 비활성화 했을 때의 비용을 최소화하여 메모리를 확보

const [n, m] = input[0].split(" ").map(Number);
const byte = input[1].split(" ").map(Number);
const price = input[2].split(" ").map(Number);

// 총 비용의 최댓값을 구합니다.
const maxCost = price.reduce((acc, curr) => acc + curr, 0);
let dp = Array(maxCost + 1).fill(0);

// 동적 프로그래밍을 사용하여 최소 비용을 계산
for (let i = 0; i < n; i++) {
  const b = byte[i]; // 메모리
  const p = price[i]; // 비용
  for (let j = maxCost; j >= p; j--) {
    dp[j] = Math.max(dp[j], dp[j - p] + b);
  }
}

// 최소 비용을 찾기 위해 dp 배열을 탐색
let result = maxCost + 1;
for (let i = 0; i <= maxCost; i++) {
  if (dp[i] >= m) {
    result = i;
    break;
  }
}

console.log(result);
