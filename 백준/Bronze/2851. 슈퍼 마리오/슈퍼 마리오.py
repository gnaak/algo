# 슈퍼 마리오

mush = [int(input()) for _ in range(10)]
tot_mushroom = [0]*10
tot_mushroom[0] = mush[0]
diff = abs(100 - mush[0])
ans = tot_mushroom[0]
for i in range(1,10):
    tot_mushroom[i] = tot_mushroom[i-1] + mush[i]
    if abs(100-tot_mushroom[i]) <= diff :
        diff = abs(100-tot_mushroom[i])
        ans = tot_mushroom[i]

print(ans)