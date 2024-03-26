function solution(brown, yellow) {
    let total = brown + yellow
    var answer = [];
    for (let x =1; x<=(yellow)**0.5; x++){
        if (yellow%x === 0){
            let y = yellow/x
            if ((x+y+2)*2 === brown){
                answer.push(y+2)
                answer.push(x+2)
            }
        }
    }
    return answer;
}