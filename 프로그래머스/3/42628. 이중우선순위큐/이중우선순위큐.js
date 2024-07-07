function solution(operations) {
  // I 숫자 -> 주어진 숫자를 삽입
  // D 1 큐에서 최대값 삭제
  // D-1 큐에서 최소값 삭제
  var answer = [];
  for (let operation of operations) {
    const [op, num] = operation.split(" ");
    if (op == "I") {
      answer.push(num);
      answer.sort((a, b) => a - b);
    } else {
      if (answer.length) {
        if (num == 1) {
          answer.pop();
        } else {
          answer.shift();
        }
      }
    }
  }
    const real =[]
    if (answer.length){
        return [Math.max(...answer), Math.min(...answer)]
    }else{
        return [0,0]
    }
}
