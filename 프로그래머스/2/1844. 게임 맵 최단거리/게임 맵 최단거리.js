function solution(maps) {
  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];
  const n = maps.length;
  const m = maps[0].length;

  function bfs() {
    let q = [];
    q.push([0, 0]);

    while (q.length) {
      const [y, x] = q.shift();

      // 목적지에 도달했을 때 거리 반환
      if (y === n - 1 && x === m - 1) {
        return maps[y][x];
      }

      for (let i = 0; i < 4; i++) {
        let ny = y + dy[i];
        let nx = x + dx[i];

        // 범위 확인
        if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
          // 방문하지 않았고 이동 가능한 경우
          if (maps[ny][nx] === 1) {
            q.push([ny, nx]);
            maps[ny][nx] = maps[y][x] + 1; // 이동 거리 계산하여 저장
          }
        }
      }
    }

    return -1; // 도달할 수 없는 경우
  }

  let answer = bfs();
  return answer;
}
