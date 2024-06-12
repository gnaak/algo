import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 문자열의 개수 n, m
s = set() # 집합 s에 같은 문자열이 주어지는 경우는 없다
for _ in range(n):
    s.add(input().strip()) # n개의 문자열로 이루어진 집합 s

cnt = 0
for _ in range(m):
    if input().strip() in s:
        cnt += 1

print(cnt)
