import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
cards = deque([i for i in range(1,n+1)]) # 1부터 n까지 카드 더미

while len(cards) > 1 : # 마지막 카드가 남을 때 까지
    cards.popleft() # 맨 밑에 카드를 버리고,
    a = cards.popleft() # 그 다음 맨 밑에 카드를
    cards.append(a) # 맨 위로 올리기

print(*cards)