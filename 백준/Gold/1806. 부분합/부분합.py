

n, s = map(int,input().split())
elements = list(map(int,input().split()))
cnt = 1e9
end = 0
tot_sum = 0
for start in range(n):
    while tot_sum < s and end < n:
        tot_sum += elements[end]
        end += 1
    if tot_sum >= s and end - start < cnt :
        cnt = end - start
    tot_sum -= elements[start]

print(cnt if cnt != 1e9 else 0)
