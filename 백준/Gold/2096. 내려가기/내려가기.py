import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())
sa, sb, sc = a, b, c

for _ in range(1, n):
    na, nb, nc = map(int, input().split())
    a, b, c = max(a, b) + na, max(a, b, c) + nb, max(b, c) + nc
    sa, sb, sc = min(sa, sb) + na, min(sa, sb, sc) + nb, min(sb, sc) + nc

print(max(a, b, c), min(sa, sb, sc))
