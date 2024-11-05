import sys
input = sys.stdin.readline

n, m = map(int,input().split())
books = list(map(int,input().split()))
total = 0
cnt = 0
for i in range(n):
    if total + books[i] <= m:
        total += books[i]
    else:
        cnt += 1
        total = books[i]

if total > 0 :
    cnt += 1

print(cnt)