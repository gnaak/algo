# 0과 1로 이루어진 문자열 S
# 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 수를 모두 뒤집는 것

import sys
input = sys.stdin.readline

zeros = 0
ones = 0
s = input().strip()

for i in range(len(s)):
    if i == 0 :
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
    else:
        if s[i] != s[i-1]:
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1

print(min(ones, zeros))