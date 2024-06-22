import math
import sys
input = sys.stdin.readline

n = int(input()) # 게임 수
# 게임은 상근이가 먼저 시작

dp = [0]*1001
# 상근이가 이길 땐 1, 창영이가 이길 땐 0
# 상근이가 먼저 시작하므로 1, 3, 4는 상근이가 이김

dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

# 상근이가 돌을 1개, 3개, 4개 집어갔을 때 창영이가 이기려면,
# 현재 돌 - 1개, 3개, 4개 일 때 모두 상근이가 이겼으면 창영이가 이긴다
# ex n = 7 일때, dp[6], dp[4], dp[3] 은 1인데,
# 상근이가 몇 개를 가져가던지 창영이는 돌 3, 4 ,6개로 게임을 먼저 시작하는 거랑 같다
for i in range(5,n+1):
    if dp[i-1] + dp[i-3] + dp[i-4] == 3:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1 :
    print('SK')
else:
    print('CY')