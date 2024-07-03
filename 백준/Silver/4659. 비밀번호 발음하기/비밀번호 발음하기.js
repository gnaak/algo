const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const vowels = ["a", "e", "i", "o", "u"];

function isVowel(char) {
  return vowels.includes(char);
}

function checkPassword(word) {
  let hasVowel = false;
  let vowelCount = 0;
  let consonantCount = 0;
  let prevChar = "";

  for (let i = 0; i < word.length; i++) {
    const char = word[i];

    if (isVowel(char)) {
      hasVowel = true;
      vowelCount++;
      consonantCount = 0;
    } else {
      vowelCount = 0;
      consonantCount++;
    }

    if (vowelCount >= 3 || consonantCount >= 3) {
      return false;
    }

    if (char === prevChar && char !== "e" && char !== "o") {
      return false;
    }

    prevChar = char;
  }

  if (!hasVowel) {
    return false;
  }

  return true;
}

for (let i = 0; i < input.length; i++) {
  const word = input[i];
  if (word === "end") break;
  if (checkPassword(word)) {
    console.log(`<${word}> is acceptable.`);
  } else {
    console.log(`<${word}> is not acceptable.`);
  }
}
