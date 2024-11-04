n = int(input())
b = list(map(int,input().split()))
b.sort()
if n == 1 :
    print(b[0]*b[0])
else:
    print(b[0]*b[-1])
