function solution(clothes) {
    let answer = 1;
    const closet = new Map();
    
    // 의상의 종류별로 의상의 개수를 세는 과정
    for (let i = 0; i < clothes.length; i++) {
        const [, type] = clothes[i]; // 의상의 종류를 가져옵니다.
        if (closet.has(type)) {
            closet.set(type, closet.get(type) + 1); // 이미 있는 종류일 경우 개수를 1 증가시킵니다.
        } else {
            closet.set(type, 1); // 새로운 종류일 경우 개수를 1로 설정합니다.
        }
    }

    // 각 종류별로 선택하는 경우의 수를 계산하여 모든 경우의 수를 곱합니다.
    for (let count of closet.values()) {
        answer *= (count + 1); // 해당 종류의 의상을 선택하지 않는 경우도 고려하여 +1을 합니다.
    }

    // 아무 것도 선택하지 않은 경우를 제외합니다.
    answer--;

    return answer;
}