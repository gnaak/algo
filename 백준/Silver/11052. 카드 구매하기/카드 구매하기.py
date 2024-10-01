# 민규는 카드의 개수가 적은 팩이라도 가격이 비싸면 높은 등급의 카드가 들어있다고 믿음
# 가장 비싼 카드를 사려고 한다는건가 ?
# 카드팩에 포함된 카드 개수의 합은 n개여야함

import sys
input = sys.stdin.readline

n = int(input()) # 필요한 카드의 개수
cards = [0]+ list(map(int,input().split()))
values = [0]*(n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        values[i] = max(values[i], values[i-j]+cards[j])

print(values[n])