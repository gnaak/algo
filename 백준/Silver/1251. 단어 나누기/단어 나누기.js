const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const word = input[0];

arr = []
for (let i = 1; i < word.length - 1; i++) {
  for (let j = i + 1; j < word.length; j++) {
    const part1 = word.slice(0, i).split("").reverse().join("");

    const part2 = word.slice(i, j).split("").reverse().join("");

    const part3 = word.slice(j).split("").reverse().join("");
    const wordReversed = part1 + part2 + part3
    arr.push(wordReversed)
  }
}

console.log(arr.sort()[0])