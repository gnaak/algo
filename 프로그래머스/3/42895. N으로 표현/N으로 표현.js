function solution(n, number) {
    let answer = -1; // 초기값을 -1로 설정하여 최소값을 찾는 문제에 대응
    
    // dp 배열 초기화
    const dp = new Array(9).fill().map(() => new Set());
    
    // 초기화: 1부터 8까지의 각 dp[i]에 n을 i개 사용하여 만들 수 있는 숫자 추가
    for (let i = 1; i <= 8; i++) {
        dp[i].add(parseInt('1'.repeat(i)) * n);
    }
    
    // dp 배열 채우기
    for (let i = 1; i <= 8; i++) {
        for (let j = 1; j < i; j++) { // j는 1부터 i-1까지
            for (const op1 of dp[j]) {
                for (const op2 of dp[i - j]) {
                    dp[i].add(op1 + op2); // 덧셈
                    dp[i].add(op1 - op2); // 뺄셈
                    dp[i].add(op1 * op2); // 곱셈
                    if (op2 !== 0) {
                        dp[i].add(Math.floor(op1 / op2)); // 나눗셈 (op2가 0이 아닐 때만)
                    }
                }
            }
        }
        // dp[i]에 number가 포함되어 있는지 확인
        if (dp[i].has(number)) {
            answer = i; // 최소 사용 횟수 갱신
            break; // answer가 갱신되면 더 이상 탐색할 필요 없음
        }
    }
    
    console.log(dp); // dp 배열 출력
    
    return answer;
}

// 테스트
console.log(solution(5, 3)); // 예상 출력: dp 배열이 출력될 것이며, 최종적인 반환 값은 answer에 의해 반환될 것임
