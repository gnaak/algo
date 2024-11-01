def solution(people, limit):
    left = 0 
    right = len(people) -1 
    ans = 0 
    people.sort()
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -=1 
        else:
            right -= 1
        ans += 1
    return ans