function solution(priorities, location) {
    var answer = 0;
    let queue = []
    for (let i=0; i<priorities.length; i++){
        queue.push({priority : priorities[i],location : i})
    }


    while (queue.length > 0){
        let first = queue.shift()
        let isHigher = false
        for (p of queue){
            if (first.priority < p.priority){
                isHigher=true;
                break
            }
        }
        if (isHigher){
            queue.push(first)
        }
        else{
            answer ++
            if (first.location === location){
                return answer
            }
        }
    }
    
    return answer;
}