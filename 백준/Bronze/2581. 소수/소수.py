'''
백준 브론즈 2
소수
'''

m = int(input())
n = int(input())
ans = []
for i in range(m, n+1):
    if i > 1:
        for j in range(2, i):
            if i%j ==0:
                break
        else:
            ans.append(i)

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)