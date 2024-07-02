const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const [n, t] = input[0].split(" ").map(Number); // n은 시험 단원의 개수, t는 공부할 수 있는 총 시간
let scores = Array(t+1).fill(0)
for (let i = 1; i <= n; i++) {
  const [time, score] = input[i].split(" ").map(Number);
  for (let j = t; j >= time; j--){
    scores[j] = Math.max(scores[j], scores[j-time] + score)
  }
}
console.log(scores[t])
