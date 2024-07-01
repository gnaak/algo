const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const tc = input[0]

let index = 1;
for (let t = 1; t <= tc; t++) {
  const n = input[index]; 
  index++;

  const coins = input[index].split(" ").map(Number); 
  index++;

  const m = Number(input[index]); 
  index++;
  let dp = Array(m + 1).fill(0) // 만드는 방법의 수 
  dp[0] = 1 // 0원을 만드는 방법은 하나도 안사용했을 때

  for (coin of coins) {
    for (let j = coin; j <= m; j++){
      dp[j] += dp[j-coin]
    }
  }
  
  console.log(dp[m])
 
}