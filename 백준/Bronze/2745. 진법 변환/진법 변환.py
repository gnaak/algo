# 진법 변환

b, n = input().split()

ans = 0
current = 0
while current < len(b):
    a = b[current]
    if a.isalpha():
        a = ord(a) - 55
    else:
        a = int(a)
    ans += a*(int(n)**(len(b)-current-1))
    current += 1

print(ans)
