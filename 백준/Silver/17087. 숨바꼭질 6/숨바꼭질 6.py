import sys
input = sys.stdin.readline
import math
n, s = map(int,input().split())
bro = list(map(int,input().split()))
dist = []

for br in bro:
    dist.append(abs(s-br))

ans = dist[0]
for i in range(1,n):
    ans = math.gcd(ans, dist[i])

print(ans)