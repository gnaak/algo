n = int(input()) # 배열 크기
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

min_cnt = 1e9
for i in range(n):
    cnt = 0
    for j in range(nums[i], nums[i]+5):
        if j not in nums:
            cnt +=1
    min_cnt = min(cnt, min_cnt)

print(min_cnt)