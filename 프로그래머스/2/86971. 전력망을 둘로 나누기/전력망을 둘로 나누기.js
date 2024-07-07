function solution(n, wires) {
  function bfs(graph, idx, cnt) {
    q = [];
    visited = Array(n).fill(0);
    q.push(idx);
    visited[idx] = 1;

    while (q.length) {
      s = q.shift();
      for (next of graph[s]) {
        if (visited[next] == 0) {
          q.push(next);
          visited[next] = 1;
          cnt++;
        }
      }
    }
    return cnt;
  }

  function makeGraph(n, wire) {
    let graph = Array.from({ length: n }, () => []); // 배열을 n개의 빈 배열로 초기화
    for ([s, e] of wire) {
      graph[s - 1].push(e - 1);
      graph[e - 1].push(s - 1);
    }
    return graph;
  }

  let answer = n;

  for (let i = 0; i < n; i++) {
    let wire = [...wires.slice(0, i), ...wires.slice(i + 1)];
    let one = bfs(makeGraph(n, wire), i, 1);
    answer = Math.min(answer, Math.abs(n - one - one));
  }

  return answer;
}
