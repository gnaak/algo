# 동전 2
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서 가치의 합이 k가 되도록
# 그러면서 동전의 개수는 최소가 되도록한다.

import sys
input = sys.stdin.readline
inf = 1e9

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
total = [inf]*(k+1)
total[0]=0

for coin in coins:
    for i in range(coin,k+1):
        total[i] = min(total[i-coin]+1, total[i])


print(total[k] if total[k]!=inf else -1)