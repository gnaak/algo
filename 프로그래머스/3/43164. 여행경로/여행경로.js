function solution(tickets) {
    const answer = [];

    // tickets를 알파벳 순으로 정렬하기
    tickets.sort();

    function dfs(current, path, usedTickets) {
        // 모든 항공권을 사용한 경우, 현재 경로를 정답으로 설정
        if (path.length === tickets.length + 1) {
            answer.push(path.slice()); // 경로 복사
            return;
        }

        for (let i = 0; i < tickets.length; i++) {
            // 사용하지 않은 항공권 중에서 현재 공항에서 출발하는 항공권을 찾음
            if (!usedTickets[i] && tickets[i][0] === current) {
                usedTickets[i] = true; // 해당 항공권을 사용 표시
                dfs(tickets[i][1], [...path, tickets[i][1]], usedTickets); // 다음 공항으로 DFS 진행
                usedTickets[i] = false; // 백트래킹: 다른 경로를 탐색하기 위해 사용 표시 해제
            }
        }
    }

    // "ICN" 공항에서 출발하여 DFS 시작
    dfs("ICN", ["ICN"], Array(tickets.length).fill(false));

    // 알파벳 순으로 가장 빠른 경로를 선택
    answer.sort();

    return answer[0]; // 가장 빠른 경로 반환
}

// Example 1
const tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]];
console.log(solution(tickets1)); // Output: ["ICN", "JFK", "HND", "IAD"]

// Example 2
const tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]];
console.log(solution(tickets2)); // Output: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
