function solution(A, B) {
    let answer = 0;

    // 배열 A는 오름차순으로 정렬합니다.
    A.sort((a, b) => a - b);

    // 배열 B는 내림차순으로 정렬합니다.
    B.sort((a, b) => b - a);

    // 각 배열의 같은 인덱스에 위치한 요소를 곱한 값을 더합니다.
    for (let i = 0; i < A.length; i++) {
        answer += A[i] * B[i];
    }

    return answer;
}
