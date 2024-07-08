const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = (depth) => {
  if (depth == m) {
    answer.add(tmp.join(' '))
    return
  }

  for (let i = 0; i < n; i++){
    if (!check[i]){
      tmp.push(arr[i])
      check[i] = 1
      f(depth + 1)
      check[i] = 0 
      tmp.pop()}
  }
  
}


const [n, m] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)
arr.sort((a, b) => a - b)
let check = Array(n).fill(0)
let tmp = []
let answer = new Set()
f(0)
answer = [...answer]
console.log(answer.join('\n'));