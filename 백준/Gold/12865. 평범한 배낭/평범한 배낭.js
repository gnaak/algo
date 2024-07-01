const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input[0].split(' ').map(Number) // 물품의 수 n, 버틸 수 있는 무게 m
let dp = Array.from({ length: m + 1 }, () => 0)

for (let i = 1; i <= n; i++){
  const [w, v] = input[i].split(' ').map(Number) // 물품의 무게 w, 가치 v
  for (let j = m; j >= w; j--){
    dp[j] = Math.max(dp[j], dp[j-w]+v)
  }
}

console.log(dp[m])

