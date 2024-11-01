# 기상청 인턴 신현수

n, x = map(int,input().split())
temp = list(map(int,input().split()))
stand = sum(temp[:x])
max_temp = stand
for i in range(x,n):
    stand += temp[i] - temp[i-x]
    if max_temp < stand:
        max_temp = stand

print(max_temp)