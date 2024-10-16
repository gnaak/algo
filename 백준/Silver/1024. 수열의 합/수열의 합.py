# 수열의 합

# n, l이 주어질 때 합이 n이면서, 길이가 적어도 l인 가장 짧은 연속된 음이 아닌 정수 리스트

import sys
input = sys.stdin.readline

n, l = map(int,input().split())
for i in range(l, 101):
    x = n/i - (i+1)/2
    if int(x) == x:
        x = int(x)
        if x + 1 >= 0:
            for j in range(x+1, x+i+1):
                print(j, end=" ")
            break
else:
    print(-1)