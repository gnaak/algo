import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n : 수열의 길이, k : 최대 삭제할 수 있는 수
s = list(map(int, input().split())) # 수열 s

# 1번 삭제했을 때 값은 0번 삭제했을 때 값에 이어서 추가되므로 dp 사용

dp = [[0 for _ in range(k+1)] for _ in range(n)]
# [0 for _ in range(k+1)] 0번, 1번 ... k 번 삭제했을 때 연속된 부분 카운팅
# [[] for _ in range(n)] 수열의 끝까지 순회

if s[0] %2 == 0 : # 처음 시작이 짝수면,
    dp[0][0] = 1 # 0번 잘라도 배열의 크기는 1
    # 오히려 자르면  ex) dp[0][1]는 0이됨 ?

for i in range(1,n): # 1번 인덱스부터에 대해서는,
    for j in range(k+1):
        if s[i] %2 == 0 :
            dp[i][j] = dp[i-1][j] + 1 # 자르지 않아도 연속되는 값이 1 증가함
        elif s[i] %2 != 0 and j != 0: # 홀수이고, 한번도 자른 적이 없지 않으면
            # 밑에 j-1 고려해서 j가 0이면 안되는데...
            dp[i][j] = dp[i-1][j-1] # 홀수여서 j를 하나 증가시켜서 삭제해도 이전과 동일 (유지)

max_cnt = 0
for i in dp:
    if max_cnt < max(i): 
        max_cnt = max(i)


print(max_cnt)
