const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);

const countries = [];
for (let i = 1; i <= N; i++) {
  const [num, gold, silver, bronze] = input[i].split(" ").map(Number);
  countries.push({ num, gold, silver, bronze });
}

countries.sort((a, b) => {
  if (a.gold !== b.gold) return b.gold - a.gold;
  if (a.silver !== b.silver) return b.silver - a.silver;
  return b.bronze - a.bronze;
});

let rank = 1;
const ranks = Array(N + 1).fill(0);
ranks[countries[0].num] = rank;

for (let i = 1; i < N; i++) {
  if (
    countries[i].gold === countries[i - 1].gold &&
    countries[i].silver === countries[i - 1].silver &&
    countries[i].bronze === countries[i - 1].bronze
  ) {
    ranks[countries[i].num] = rank;
  } else {
    rank = i + 1;
    ranks[countries[i].num] = rank;
  }
}

console.log(ranks[K]);
