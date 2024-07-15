const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const bfs = () => {
  q = [];
  q.push(1);

  while (q.length) {
    const current = q.shift();
    for (child of graph[current]) {
      if (parent[child] == 0) {
        parent[child] = current;
        q.push(child);
      }
    }
  }
};

const node = Number(input[0]);
let graph = Array.from({ length: node + 1 }, () => []);
let parent = Array.from({ length: node + 1 }, () => [0]);

for (let i = 1; i < input.length; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

bfs();
for (let i = 2; i < parent.length; i++) {
  console.log(parent[i]);
}
