const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// D : D는 값을 2배로 바꾼다
// S : S는 n에서 1을 뺀 결과를 저장 만약 n이 0이면 9999 저장
// L : L은 각 자리수를 왼편으로 회전
// R : R은 각 자리수를 오른편으로 회전
// L && R 사용 시 n에 0이 포함된 경우 주의

const bfs = (a, b) => {
  let q = [];
  q.push([a, ""]);
  let visited = Array(10000).fill(false);
  visited[a] = true;
  
  while (q.length > 0) {
    const [current, path] = q.shift();
    if (current == b) return path;
    
    const d = (current * 2) % 10000;
    if (!visited[d]) {
      visited[d] = true;
      q.push([d, path + "D"]);
    }
    
    let s = current === 0 ? 9999 : current - 1;
    if (!visited[s]) {
      visited[s] = true;
      q.push([s, path + "S"]);
    }
    
    const l = (current % 1000) * 10 + Math.floor(current / 1000);
    if (!visited[l]) {
      visited[l] = true;
      q.push([l, path + "L"]);
    }
    
    const r = (current % 10) * 1000 + Math.floor(current / 10);
    if (!visited[r]) {
      visited[r] = true;
      q.push([r, path + "R"]);
    }
  }
};

const tc = Number(input[0]);
const results = [];
for (let i = 1; i <= tc; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  results.push(bfs(a, b));
}
console.log(results.join("\n"));
