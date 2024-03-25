function solution(numbers, target) {
    let answer = 0;
    const n = numbers.length;
    
    const dfs = (index, sum) => {
        if (index == n) {
            if (sum == target) {
                answer += 1;
            }
            return;
        }
        
        dfs(index + 1, sum + numbers[index]); // 현재 숫자를 더하는 경우
        dfs(index + 1, sum - numbers[index]); // 현재 숫자를 빼는 경우
    }
    
    dfs(0, 0); // 초기 인덱스와 합계는 0부터 시작합니다.
    
    return answer;
}
