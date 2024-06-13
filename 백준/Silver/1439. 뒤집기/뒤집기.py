import sys
input = sys.stdin.readline

n = str(input().strip())
cnt = [0,0]
cnt[int(n[0])] += 1
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        cnt[int(n[i])]+=1
    elif i == len(n):
        cnt[int(n[-1])] +=1

print(min(cnt))