def solution(nums):
    a = len(set(nums))
    if len(nums) / 2 <=  a:
        return len(nums) / 2 
    else:
        return a 
