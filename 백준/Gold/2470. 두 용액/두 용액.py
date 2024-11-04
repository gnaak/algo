# 두 용엑

n = int(input())
liq = list(map(int,input().split()))
dif = float('inf')
liq.sort()

start = 0
end = n - 1
ans = []

while start < end :
    tot = liq[start] + liq[end]
    if abs(dif) > abs(tot):
        dif = tot
        ans = [liq[start], liq[end]]

    if tot < 0 :
        start += 1
    else:
        end -= 1

print(*ans)