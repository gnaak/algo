n = int(input()) # 타겟 목표
start = 1
end = 2
cnt = 0
ans = 3
while end < n and start < end:
    if ans == n :
        cnt +=1
        ans -= start
        start +=1
    elif ans > n :
        ans -=start
        start+=1
    else:
        end +=1
        ans+= end
print(cnt+1)