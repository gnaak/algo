'''
백준 브론즈2
분해합
'''

n = int(input())
ans = 0
for i in range(1, n+1):
    num = sum((map(int,str(i))))
    total = num + i
    if total == n :
        ans = i
        break

print(ans)