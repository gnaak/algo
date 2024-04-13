'''
백준 실버 3
두 수의 합
'''

n = int(input()) # 수열의 크기 n
nums = list(map(int,input().split())) # 수열에 담길 수
x = int(input()) # 만족해야 하는 숫자
nums.sort()
cnt = 0
start = 0
end = n-1
while start < end:
    ans = nums[start]+nums[end]
    if ans == x:
        cnt +=1
        end -=1
    elif ans < x:
        start+=1
    else:
        end-=1

print(cnt)