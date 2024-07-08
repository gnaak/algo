const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = (depth) => {
  if (depth == m) {
    output += tmp.join(' ')
    output += '\n'
    return
  }

  for (let i = 0; i < n; i++){
      tmp.push(arr[i])
      f(depth + 1)
      tmp.pop()

  }
  
}


const [n, m] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)
arr.sort((a,b)=>a-b)
let tmp = []
let check = Array(n).fill(0)
let output = ''
f(0)
console.log(output)