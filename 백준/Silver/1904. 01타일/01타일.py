def count_num(n) :
    MOD = 15746
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    else:
        prev2 = 1
        prev1 = 2
        current = 0

        for i in range(3, n+1):
            current = (prev2 + prev1) % 15746
            prev2 = prev1
            prev1 = current
            
    return current 

import sys
input = sys.stdin.readline

n = int(input())
print(count_num(n))