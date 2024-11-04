# 16 진수

words = input().strip()
jinsu = {'A':10, 'B':11, 'C':12,'D':13,'E':14,'F':15}

ans = 0
current = 0
while current < len(words):
    a = words[current]

    if a in jinsu:
        a = jinsu[a]

    ans += int(a)*(16**(len(words)-current-1))
    current +=1

print(ans)