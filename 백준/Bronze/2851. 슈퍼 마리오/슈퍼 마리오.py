# 슈퍼 마리오

import sys
input = sys.stdin.readline


tot_mushroom = [0]*10
diff = 100
ans = 0
for i in range(10):
    mushroom = int(input())
    if i == 0 :
        tot_mushroom[0] = mushroom
    else:   
        tot_mushroom[i] = tot_mushroom[i-1] + mushroom

    if abs(100-tot_mushroom[i]) <= diff:
        diff = abs(100-tot_mushroom[i])
        ans = tot_mushroom[i]

print(ans)

