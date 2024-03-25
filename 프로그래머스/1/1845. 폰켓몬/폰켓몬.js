function solution(nums) {
    let answer = [...new Set(nums)]
    if (answer.length > nums.sort().length/2){
        return nums.sort().length/2
    }
    return answer.length;
}

