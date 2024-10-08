import sys
input = sys.stdin.readline

num = input().strip()
ans = 0
while int(num) >= 10 :
    new_num = 0
    for i in range(len(num)):
        new_num += int(num[i])

    num = str(new_num)
    ans += 1

print(ans)
print("YES" if int(num) % 3 == 0 else "NO")