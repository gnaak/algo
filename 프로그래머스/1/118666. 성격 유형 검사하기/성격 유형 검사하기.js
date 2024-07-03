function solution(survey, choices) {
  const mbti = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };
  const score = { 1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3 };
  for (let i = 0; i < survey.length; i++) {
    mbti[survey[i][0]] += score[choices[i]];
  }
  console.log(mbti);
  var answer = "";
  if (mbti['R'] >= mbti['T']) answer += 'R';
  if (mbti['R'] < mbti['T']) answer += 'T';
  if (mbti['C'] >= mbti['F']) answer += 'C';
  if (mbti['C'] < mbti['F']) answer += 'F';
  if (mbti['J'] >= mbti['M']) answer += 'J';
  if (mbti['J'] < mbti['M']) answer += 'M';
  if (mbti['A'] >= mbti['N']) answer += 'A';
  if (mbti['A'] < mbti['N']) answer += 'N';
  return answer;
}
