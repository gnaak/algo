'''
백준 브론즈 2
수학은 비대면강의입니다
'''

nums = list(map(int,input().split()))

for i in range(-999,1000):
    for j in range(-999,1000):
        if nums[0]*i + nums[1]*j == nums[2] and nums[3]*i + nums[4]*j == nums[5]:
            print(i, j)