const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [a, b] = input[0].split(" ").map(Number);
const tmp = []

function f() {
  if (tmp.length == b) {
    console.log(tmp.join(' '))
    return
  }

  else {
    for (let i = 1; i <= a; i++){
      if (!tmp.includes(i)) {
        tmp.push(i)
        f()
        tmp.pop()
      }
    }
  }
}

f()