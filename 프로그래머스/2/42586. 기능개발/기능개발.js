function solution(progresses, speeds) {
    var answer = [];
    const n = speeds.length
    const days = new Array(n).fill()
    for(let i=0; i<n; i++){
        const leftOver = Math.ceil((100-progresses[i])/speeds[i])
        days[i] = leftOver
    }
    console.log(days)
    let cnt = 1 
    let current = days.shift()
    while (days.length > 0){
        if (current >= days[0]){
            cnt+=1
            days.shift()
        }
        else{
            answer.push(cnt)
            cnt = 1
            current = days.shift()
        }
    }
    answer.push(cnt)
    console.log(answer)
    return answer;
}