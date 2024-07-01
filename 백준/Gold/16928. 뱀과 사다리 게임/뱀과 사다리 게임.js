const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const bfs = (start, end) => {
  const queue = [];
  queue.push(start);
  visited[start] = 0;

  while (queue.length > 0) {
    const current_idx = queue.shift();
    if (current_idx === end) {
      return visited[end];
    }
    for (let i = 1; i <= 6; i++) {
      let next_idx = current_idx + i;
      if (next_idx <= 100 && visited[next_idx] == 0) {
        if (t[next_idx]) {
          next_idx = t[next_idx]
        }
        if (visited[next_idx] === 0) {
          queue.push(next_idx);
          visited[next_idx] = visited[current_idx] + 1;
        }
      }
    }
  }
};

// 100번 칸을 넘어간다면 이동할 수 없다.
const [n, m] = input[0].split(" ").map(Number); // 게임 판에 있는 사다리의 수 n, 뱀의 수 m
const t = {};
for (let i = 1; i <= n + m; i++) {
  const [s, e] = input[i].split(" ").map(Number);
  t[s] = e;
}
const visited = Array(101).fill(0);

let start = 1;
const end = 100;
console.log(bfs(start, end));
