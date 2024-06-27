function solution(friends, gifts) {
    const n = friends.length;
    const gift_lst = {};
    const gift_zisu = {};
    friends.forEach((friend, i) => {
        gift_lst[friend] = i;
        gift_zisu[friend] = 0;
    });

    const graph = Array.from({ length: n }, () => Array(n).fill(0));

    gifts.forEach(gift => {
        const [send, receive] = gift.split(" ");
        graph[gift_lst[send]][gift_lst[receive]] += 1;
        gift_zisu[send] += 1;
        gift_zisu[receive] -= 1;
    });

    const answer = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i !== j) {
                if (graph[i][j] > graph[j][i]) {
                    answer[i] += 1;
                } else if (graph[i][j] === graph[j][i]) {
                    if (gift_zisu[friends[i]] > gift_zisu[friends[j]]) {
                        answer[i] += 1;
                    }
                }
            }
        }
    }

    return Math.max(...answer);
}
