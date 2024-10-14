# 통계학

# 1. 산술평균 : n개의 수들의 합을 n으로 나눔
# 2. 중앙값 : n개의 수들을 증가하는 순서로 나열했을 때 중앙에 위치하는 값
# 3. 최반값 : n개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : n개의 수들 중 최댓값과 최솟값의 차이

import sys
input = sys.stdin.readline

nums = []
nums_dict = dict()
n = int(input()) # n개의 수
for _ in range(n):
    a = int(input())
    nums.append(a)
    if a in nums_dict:
        nums_dict[a] +=1
    else:
        nums_dict[a] = 1

nums.sort()

# 산술평균
print(round(sum(nums)/n))

# 중앙값
print(nums[n//2])

# 최빈값
small = []
mx = max(nums_dict.values())
for number, times in nums_dict.items():
    if times == mx:
        small.append(number)

small.sort()

if len(small) == 1:
    print(small[0])
else:
    print(small[1])

# 범위
print(nums[-1] - nums[0])