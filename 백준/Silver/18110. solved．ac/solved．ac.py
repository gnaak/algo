# solved.ac

# 아직 아무 의견이 없다면, 문제의 난이도는 0
# 의견이 하나 이상 있으면, 모든 사람의 의견의 30% 절사평균으로 결정
# 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것

import sys
input = sys.stdin.readline

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

n = int(input())
scores = [int(input()) for _ in range(n)]
scores.sort()
if n == 0 :
    print(0)
else:
    a = my_round(n*0.15)
    if a > 0 :
        scores = scores[a:-a]
    print(my_round(sum(scores)/len(scores)))
