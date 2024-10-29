import sys
input = sys.stdin.readline

n = int(input())

num = 0
cycle = 0
a = n
if n == 0 :
    print(1)
else:
    while num != a :
        if n < 10:
            n = n * 11
        else:
            n = n % 10 * 10 + (n // 10 + n % 10) % 10

        num = n
        cycle +=1

    print(cycle)