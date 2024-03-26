function solution(answers) {
    var answer = [];
    let ans_1 = [1,2,3,4,5]
    let ans_2 = [2,1,2,3,2,4,2,5]
    let ans_3 = [3,3,1,1,2,2,4,4,5,5]
    let score = [0,0,0]
    for (let i=0; i<answers.length;i++){
        if(answers[i] === ans_1[i%ans_1.length]){
            score[0] ++
        }
        if(answers[i] === ans_2[i%ans_2.length]){
            score[1] ++
        }      
        if(answers[i] === ans_3[i%ans_3.length]){
            score[2] ++
        }
    }
    let max_scorer = Math.max(...score)
    for (let i=0; i<3;i++){
        if(score[i] === max_scorer){
            answer.push(i+1)
        }
    }
    return answer;
}

