function solution(today, terms, privacies) {
  let todayDate = today.split(".").map(String);
  let due = {};
  for (term of terms) {
    const [type, date] = term.split(" ");
    due[type] = Number(date);
  }
  var answer = [];

  for (let i = 0; i < privacies.length; i++) {
    const [date, type] = privacies[i].split(" ");
    const signed = date.split(".");
    let year = Number(signed[0]);
    let month = Number(signed[1]);
    let day = Number(signed[2]) - 1;
    month += Number(due[type]);
    if (month > 12) {
      year += Math.floor(month/12)
      month -=  Math.floor(month/12)*12
    }
    if (day == 0) {
      day = 28;
      month -= 1;
    }
    if (month == 0) {
      year -= 1;
      month = 12;
    }
    if (Number(todayDate[0]) > year) {
      answer.push(i + 1);
    } else if (Number(todayDate[0]) == year) {
      if (Number(todayDate[1]) > month) {
        answer.push(i + 1);
      } else if (Number(todayDate[1]) == month && Number(todayDate[2]) > day) {
        answer.push(i + 1);
      }
    }
  }
return answer;

}

