'''
백준 실버 2
랜선 자르기
'''

k , n = map(int,input().split()) # 가지고 있는 랜선의 개수 k, 필요한 랜선의 개수 n
wires = []  # 가지고 있는 랜선의 길이
for _ in range(k):
    wires.append(int(input()))

s = 1 # 최소 길이
e = max(wires) # 최대 길이

while s <= e:
    mid = (s+e)//2
    lan = 0
    for wire in wires:
        lan += wire // mid

    if lan >= n :
        s = mid + 1
    else:
        e = mid - 1

print(e)
