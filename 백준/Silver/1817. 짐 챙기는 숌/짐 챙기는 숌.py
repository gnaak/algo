import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stuff = list(map(int, input().split()))

# 만약 책의 개수가 0인 경우

start = 0
end = 0
cnt = 0
tot = 0

if n == 0:
    print(0)
else:
    while end < n:
        # 현재 박스에 책을 계속 추가
        if tot + stuff[end] > m:
            cnt += 1
            tot = stuff[end]
        else:
            tot += stuff[end]
        end += 1
    
    if tot > 0:
        cnt += 1
    
    print(cnt)
