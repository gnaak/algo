import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    n , m = map(int,input().split()) # 서쪽 n, 동쪽 m
    if n == m :
        print(1)
    elif n == 1 :
        print(m)
    else:
        a = 1 
        b = 1 
        for i in range(n):
            a *= (m-i)
            b *= (i+1)
        print(int(a/b))