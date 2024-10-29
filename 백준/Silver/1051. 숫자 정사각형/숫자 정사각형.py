# 숫자 정사각형

# n*m 크기의 직사각형에서 꼭지점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형의 넓이

import sys
input = sys.stdin.readline

mx = 1
n, m = map(int,input().split())
rect = [str(input().strip()) for _ in range(n)]
s = min(n, m)
for k in range(1,s+1):
    for i in range(n-k):
        for j in range(m-k):
            if i+k < n and j+k < m and rect[i][j] == rect[i+k][j] and rect[i][j] == rect[i][j+k] and rect[i][j] == rect[i+k][j+k]:
                mx = max(mx,(k+1)**2)
print(mx)