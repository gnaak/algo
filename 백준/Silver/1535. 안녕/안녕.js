const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const hello = (people, pleasure, health) => {
  if (people > n) return;
  dp[people] = Math.max(dp[people], pleasure);

  // 인사를 해도 죽지 않을 때
  if (health - h[people] > 0) {
    hello(people + 1, pleasure + p[people], health - h[people]);
  }
  // 그냥 인사 안할 때
  hello(people + 1, pleasure, health);
};


const n = Number(input[0]); // 사람의 수
const h = input[1].split(" ").map(Number); // 잃는 체력
const p = input[2].split(" ").map(Number); // 얻는 기쁨

// 사람들에게 인사했을 때, 얻을 수 있는 최대 기쁨
let dp = Array(n + 1).fill(0);
hello(0, 0, 100); // 초기 인자 설정을 잊지 않도록 주의

console.log(dp[n])