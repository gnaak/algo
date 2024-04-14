'''
백준 실버 5
배열 합치기
'''

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

idxa = 0
idxb = 0
ans = []

while True:
    if idxa == n and idxb == m:
        break
    else:
        if idxa == n:
            ans.append(b[idxb])
            idxb+=1
        elif idxb == m :
            ans.append(a[idxa])
            idxa +=1
        elif a[idxa] > b[idxb]:
            ans.append(b[idxb])
            idxb +=1
        elif a[idxa] < b[idxb]:
            ans.append(a[idxa])
            idxa +=1
        else:
            ans.append(a[idxa])
            idxa +=1


for an in ans:
    print(an,end=' ')