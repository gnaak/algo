const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const dfs = (num, wei) => {
  if (num > n) return;
  if (dp[num][wei] == 1) return
  dp[num][wei] = 1 
  dfs(num + 1, wei + ws[num]);
  dfs(num + 1, wei);
  dfs(num + 1, Math.abs(ws[num] - wei));
};

const n = Number(input[0]); // 추의 개수
const ws = input[1].split(" ").map(Number); // 추들
const m = Number(input[2]); // 확인할 추의 개수
const targets = input[3].split(" ").map(Number); // 확인할 추의 무게

const maxWeight = ws.reduce((acc, cur) => acc + cur, 0); // 모든 추들을 더한 최대 무게
let dp = Array.from({ length: n + 1 }, () => Array(maxWeight).fill(0)); // 확인이 가능하면 1, 아니면 0
dfs(0, 0);

const answer = [];

for (target of targets) {
  if (dp[n][target] === 1) answer.push("Y");
  else answer.push("N");
}

console.log(answer.join(" "));