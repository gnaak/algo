# 에라토스테네스의 체

# n보다 작거나 같은 모든 소수를 찾는 알고리즘
# 1. 2부터 n까지 모든 정수를 적는다.
# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. p
# 3. p를 지우고, 아직 지우지 않은 p의 배수를 크기 순서대로 지운다
# 4. 아직 모든 수를 지우지 않았다면, 다시 2단계로 간다.

# n, k가 주어졌을 때, k번째 지우는 수를 구하시오

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
nums = [0]*(n+1)

cnt = 0
fin = False

for i in range(2,n+1):
    if nums[i] == 0 :
        for j in range(1, n // i + 1):
            if nums[i * j] == 0:
                nums[i * j] = 1
                cnt += 1
            if cnt == k:
                print(i * j)
                fin = True
                break

    if fin:
        break
