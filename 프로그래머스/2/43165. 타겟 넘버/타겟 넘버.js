// DFS로 풀자!

// [+1, +1, +1, +1, +1]
// [+1, +1, +1, +1, -1]
// [+1, +1, +1, -1, +1]
// [+1, +1, +1, -1, -1]
// [+1, +1, -1, +1, +1]
// [+1, +1, -1, +1, -1]
// [+1, +1, -1, -1, +1]
// [+1, +1, -1, -1, -1]

// 1. 이번턴에 어떤 동작을 수행할 것인가?
// 2. 언제 탈출할 것인가?
// 3. 누적합이 target과 같다면 return

function solution(numbers, target) {
    let answer = 0;

    function DFS(sum, depth) {
        // 2)
        if(depth == numbers.length) {
            // 3)
            if(sum == target) {
                answer += 1;
            }

            return;
        }

        // 1)
        DFS(sum + numbers[depth], depth+1);
        DFS(sum - numbers[depth], depth+1);
    }

    DFS(0, 0);

    return answer;
}