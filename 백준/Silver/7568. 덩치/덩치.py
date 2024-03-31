'''
백준 실버5
덩치
'''

n = int(input())
data = []
ans = []
for _ in range(n):
    x, y = map(int,input().split())
    data.append((x,y))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count +=1
    ans.append(count+1)

for an in ans:
    print(an, end=' ')