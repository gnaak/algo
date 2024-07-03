const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, type] = input[0].split(" "); // 같이 플레이하기를 신청한 횟수, 플레이할 게임의 종류
const num = Number(n); // 같이 플레이하기를 신청한 횟수
const stringType = String(type).trim()
const type_num = {
  Y: 2,
  F: 3,
  O: 4,
};

// 임스는 한 번 같이 플레이 한 사람과는 다시 플레이하지 않는다
const player_dict = {}
for (let i = 1; i < num + 1; i++) {
  const player = input[i].trim();
  if (player_dict[player]) {
    player_dict[player]++;
  } else {
    player_dict[player] = 1;
  }
}
const playersCnt = Object.keys(player_dict).length
const required = type_num[stringType] -1
console.log(Math.floor(playersCnt / required));
