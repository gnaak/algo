'''
백준 브론즈 1
피보나치수 2
'''

n = int(input())
dp = []
for i in range(n+1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else:
        num = dp[-1]+dp[-2]
    dp.append(num)
    
print(dp[-1])