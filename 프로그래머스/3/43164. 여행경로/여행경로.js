function solution(tickets) {
    let answer = [];
    const visited = new Array(tickets.length).fill(false);
    let route = [];

    tickets.sort(); // 항공권을 알파벳 순서대로 정렬

    function dfs(current, depth) {
        route.push(current); // 경로에 현재 공항 추가

        if (depth === tickets.length) {
            if (answer.length === 0 || compareRoutes(route, answer) < 0) {
                answer = route.slice(); // 현재 경로가 알파벳 순서가 앞서는 경로이면 정답으로 선택
            }
            return;
        }

        for (let i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0] === current) {
                visited[i] = true;
                dfs(tickets[i][1], depth + 1); // 다음 공항으로 이동
                visited[i] = false;
                route.pop(); // 백트래킹: 경로에서 이전 공항 제거
            }
        }
    }

    function compareRoutes(route1, route2) {
        for (let i = 0; i < route1.length; i++) {
            if (route1[i] < route2[i]) {
                return -1; // route1이 route2보다 알파벳 순서가 앞서면 음수 반환
            } else if (route1[i] > route2[i]) {
                return 1; // route1이 route2보다 알파벳 순서가 뒤쪽이면 양수 반환
            }
        }
        return 0; // 두 경로가 동일하면 0 반환
    }

    dfs("ICN", 0); // 출발 공항은 ICN

    return answer;
}
