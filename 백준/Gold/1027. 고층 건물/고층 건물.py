# 고층 건물

import sys
input = sys.stdin.readline

n = int(input())
building = list(map(int,input().split()))
answer = 0

for i in range(n):
    temp = n - 1
    for j in range(i + 1, n):
        for k in range(i + 1, j):
            if building[k] - building[i] >= (((building[j] - building[i]) / (j - i)) * (k - i)):
                temp -= 1
                break
        # i ~ 끝 까지의 빌딩
    for j in range(0, i):
        for k in range(j + 1, i):
            if building[k] - building[j] >= (((building[i] - building[j]) / (i - j)) * (k - j)):
                temp -= 1
                break
        # 처음 부터 ~ i 빌딩 사이
    answer = max(temp, answer)
print(answer)