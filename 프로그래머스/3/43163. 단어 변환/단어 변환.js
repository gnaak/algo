function solution(begin, target, words) {
    const visited = []
    for (let i=0; i< words.length;i++){
        visited.push(0)
    }
    let answer = 0;

    function dfs(current, depth) {
        if (current === target) {
            answer = depth;
            return;
        }
        for (let i = 0; i < words.length; i++) {
            if (visited[i] === 0 && isOneDiff(current, words[i])) {
                visited[i] = 1;
                dfs(words[i], depth + 1);
                visited[i] = 0;
            }
        }
    }

    function isOneDiff(word1, word2) {
        let diff = 0;
        for (let i = 0; i < word1.length; i++) {
            if (word1[i] !== word2[i]) {
                diff++;
                if (diff > 1) {
                    return false;
                }
            }
        }
        return diff === 1;
    }

    dfs(begin, 0);
    return answer;
}
