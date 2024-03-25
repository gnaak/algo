function solution(people, limit) {
    let answer = 0;
    let left = 0;
    let right = people.length - 1;

    // 1)
    people = people.sort((a, b)=> a-b);

    // 2)
    while(left <= right) {
        if(people[left] + people[right] > limit) {
            right -= 1;
        } else if(people[left] + people[right] <= limit) {
            left += 1;
            right -= 1;
        }

        answer += 1;
    }

    return answer;
}
