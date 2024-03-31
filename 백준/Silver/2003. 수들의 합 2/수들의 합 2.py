'''
백준 실버 4
수들의 합 2
'''

n, m = map(int,input().split())
ls = list(map(int,input().split()))
left = 0
right = 1
cnt = 0
ans = ls[0]
while True:
    if ans < m :
        if right < n :
            ans+= ls[right]
            right += 1
        else:
            break
    elif ans > m:
        ans -= ls[left]
        left +=1

    elif ans == m :
        cnt +=1
        ans -= ls[left]
        left +=1

print(cnt)