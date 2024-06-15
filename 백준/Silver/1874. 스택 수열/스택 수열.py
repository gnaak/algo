import sys
input = sys.stdin.readline

n = int(input())
want = [int(input()) for _ in range(n)]

stack = []
make = []
current = 1

for num in want:
    while current <= num:
        stack.append(current)
        make.append('+')
        current += 1
    
    if stack and stack[-1] == num:
        stack.pop()
        make.append('-')
    else:
        print('NO')
        break
else:
    print("\n".join(make))
