# 요세푸스 문제

# 1번부터 N번까지 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다.
# 한 사람이 제거되면 남은 사람들로 원을 따라 이 과정을 계속해 나간다.
# 사람들이 제거되는 순서를 요세푸스 순열이라고 한다

# ex) 7, 3
# 1 2 3 4 5 6 7 -> 1 2 4 5 6 7 -> 1 2 4 5 7 -> 1 4 5 7 -> 1 4 5 -> 1 4 -> 4 ->1
# 출력은 3, 6, 2, 7, 5, 1, 4

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
players = [i for i in range(1,n+1)]
target = k-1
answer = []

for _ in range(n):
    answer.append(str(players.pop(target)))
    target += k-1
    if players :
        target %= len(players)

print('<',', '.join(answer),'>',sep='')