function solution(nums) {
    let answer = [...new Set(nums)]
    if (answer.length > nums.length/2){
        return nums.length/2
    }
    return answer.length;
}

