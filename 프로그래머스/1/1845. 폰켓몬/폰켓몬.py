def solution(nums):
    answer = len(nums)/2
    if answer > len(set(nums)):
        return len(set(nums))
    return answer