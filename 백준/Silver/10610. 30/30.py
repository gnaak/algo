import sys
input = sys.stdin.readline

n = input().strip()

tot_sum = 0
for a in n :
    tot_sum += int(a)

if "0" not in n:
    print(-1)

elif tot_sum % 3 != 0 :
    print(-1)

else:
    sorted_n = sorted(n, reverse=True)

    print(''.join(sorted_n))