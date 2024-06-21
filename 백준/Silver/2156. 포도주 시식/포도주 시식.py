import sys
input = sys.stdin.readline

n = int(input().strip())  # 포도주 잔의 개수

if n == 0:
    print(0)
    sys.exit()

wine = []
for i in range(n):
    wine.append(int(input().strip()))

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp = [0] * n  # 마신 최대 포도주

    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], wine[i] + dp[i-2], dp[i-1])

    print(max(dp))

