'''
백준 브론즈2
분해합
'''

n = int(input())

for i in range(1, n+1):
    num = sum((map(int,str(i))))
    total = num + i
    if total == n :
        print(i)
        break
else:
    print(0)