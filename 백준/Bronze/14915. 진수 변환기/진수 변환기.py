# 진수 변환기

import sys
input = sys.stdin.readline

m, n = map(int,input().split())
# m을 n진수로 변환

jinsu = {10:'A',11:'B',12:'C', 13:'D', 14:'E', 15:'F'}

ans = []

if m == 0 :
    print(0)
else:
    while m > 0 :
        a = m%n
        if a in jinsu:
            a = jinsu[a]
        ans.append(a)
    
    
        m //= n

    print(''.join(map(str,ans[::-1])))