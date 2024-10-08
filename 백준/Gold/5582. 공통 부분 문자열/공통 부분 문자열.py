# s의 부분 문자열이란, s가 t에 연속으로 나타나는 것을 의미한다.

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

lens = len(s)
lent = len(t)

dp = [[0] * (lent+1) for _ in range(lens+1)]
max_length = 0

for i in range(1,lens+1):
    for j in range(1,lent+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if max_length < dp[i][j]:
                max_length = dp[i][j]

print(max_length)
