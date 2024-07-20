const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const f = () => {
  // mid 값을 구하기 위해서 가장 짧은 길이와 가장 긴 길이
  let min = 1;
  let max = c[n - 1];

  while (min <= max) {
    let mid = Math.floor((min + max) / 2);
    // 각각의 과자 길이를 중간값으로 나누었을 때, cnt는 나누어 줄 수 있는 사람의 수
    let cnt = 0 
    for(let i = 0; i < n; i++) {
      cnt += Math.floor(c[i] / mid);
    }    // cnt가 m보다 크거나 같으면, 길이를 더 늘려서 나누어줘도 가능함
    if (cnt >= m) {
      min = mid + 1;
    } else {
      max = mid - 1;
    }
  }
  console.log(max);
};

const [m, n] = input[0].split(" ").map(Number); // m은 조카의 수, n은 과자의 수
const c = input[1].split(" ").map(Number);
c.sort((a, b) => a - b);
f(m, n, c);