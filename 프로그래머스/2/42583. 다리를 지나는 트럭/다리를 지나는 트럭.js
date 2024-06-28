function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let current = 0
    const bridge = new Array(bridge_length).fill(0)
    while (truck_weights.length > 0){
        
        answer ++;
        current -= bridge.shift();
        if (current + truck_weights[0] <= weight){
            current+=truck_weights[0]
            bridge.push(truck_weights.shift())
        }
        else{
            bridge.push(0)
    }
        }
    answer += bridge_length
    return answer;
}