import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        # 스티커가 하나만 있는 경우
        print(max(sticker[0][0], sticker[1][0]))
    else:
        dp = [[0] * n for _ in range(2)]
        
        # 첫 번째 열 초기화
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        
        if n > 1:
            # 두 번째 열 초기화
            dp[0][1] = sticker[1][0] + sticker[0][1]
            dp[1][1] = sticker[0][0] + sticker[1][1]

        # DP 테이블 채우기
        for j in range(2, n):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + sticker[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + sticker[1][j]

        # 최댓값 출력
        print(max(dp[0][n-1], dp[1][n-1]))
