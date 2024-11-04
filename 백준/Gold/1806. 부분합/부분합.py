n, s = map(int,input().split())
elements = list(map(int,input().split()))
cnt = 1e9
start = 0
end = 0
tot_sum = 0
while end < n :
    tot_sum += elements[end]
    end += 1

    while tot_sum >= s:
        if cnt > end - start:
            cnt = end - start
        tot_sum -= elements[start]
        start += 1


print(cnt if cnt != 1e9 else 0)
