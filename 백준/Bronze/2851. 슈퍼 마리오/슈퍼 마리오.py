import sys
input = sys.stdin.readline

diff = 100
tot_mush = 0
for i in range(10):
    mush = int(input())
    tot_mush += mush

    if abs(tot_mush - 100) <= diff:
        diff = abs(tot_mush-100)
    else:
        tot_mush -= mush
        break
        
print(tot_mush)