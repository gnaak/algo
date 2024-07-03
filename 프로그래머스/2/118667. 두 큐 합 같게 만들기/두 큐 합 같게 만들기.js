function solution(queue1, queue2) {
    const totalSum = (arr) => arr.reduce((acc, cur) => acc + cur, 0);

    let sum1 = totalSum(queue1);
    let sum2 = totalSum(queue2);

    const target = (sum1 + sum2) / 2;
    
    if ((sum1 + sum2) % 2 !== 0) return -1; // 두 큐의 합이 홀수면 나눌 수 없음
    
    const combinedQueue = [...queue1, ...queue2];
    let p1 = 0, p2 = queue1.length;
    let currentSum = sum1;
    let moves = 0;

    while (p1 < combinedQueue.length && p2 < combinedQueue.length) {
        if (currentSum === target) return moves;

        if (currentSum < target) {
            currentSum += combinedQueue[p2];
            p2++;
        } else {
            currentSum -= combinedQueue[p1];
            p1++;
        }
        moves++;
    }

    return -1; // 두 큐의 합을 같게 만들 수 없는 경우
}