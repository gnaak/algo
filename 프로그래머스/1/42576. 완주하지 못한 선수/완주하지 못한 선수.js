function solution(participant, completion) {
    // 참가자 명단과 완주자 명단을 각각 정렬합니다.
    participant.sort();
    completion.sort();

    // 완주자 명단과 비교하여 완주하지 못한 참가자를 찾습니다.
    for (let i = 0; i < completion.length; i++) {
        if (participant[i] !== completion[i]) {
            return participant[i];
        }
    }

    // 완주자 명단과 비교하여 맨 마지막 참가자가 완주하지 못한 참가자인 경우를 처리합니다.
    return participant[participant.length - 1];
}
