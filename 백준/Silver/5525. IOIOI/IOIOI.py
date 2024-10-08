# IOIOI

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input())

# Pn이 몇개인지 찾는 문제 -> Pn = n+1개의 I와 n개의 O로 이루어진 문자열
pn = ""
for i in range(n+1):
    pn += "I"
    if i != n:
        pn += "O"

ans = 0
for i in range(m-2*n):
    if s[i:2*n+1+i] == pn:
        ans +=1

print(ans)
