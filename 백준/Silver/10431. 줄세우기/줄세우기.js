const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const tc = Number(input[0])
let idx = 1 
for (let i = 1; i <= tc; i++){
  const student = input[idx].split(' ').map(Number)
  const number = student[0]
  let cnt = 0 
  const height = []
  for (let i = 1; i < student.length; i++){
    height.push(student[i])
  }

  for (let j = 0; j < height.length -1; j++){
    for (let k = j+1 ; k < height.length ; k++){
      if (height[j] > height[k]) {
        height[j], height[k] = height[k], height[j] 
        cnt += 1
      }
    }
  }

  console.log(number, cnt)

  idx += 1
}