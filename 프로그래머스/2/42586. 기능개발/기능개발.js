function solution(progresses, speeds) {
    var answer = [];
    let total = 100;
    let queue = []
    for (let i=0; i<speeds.length; i++){
        queue.push(Math.ceil((total-progresses[i])/speeds[i]))
    }
    let cnt = 1
    let current = queue.shift()
    while (queue.length > 0){
        if (current >= queue[0]){
            cnt+=1
            queue.shift()
        }
        else{
                        answer.push(cnt);
            cnt = 1
            current = queue.shift()
        }
    }
    answer.push(cnt)
    return answer;
}



