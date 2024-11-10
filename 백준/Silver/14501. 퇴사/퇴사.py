# 퇴사
# n+1 일째 되는 날 퇴사를 하기 위해서 n일 동안 최대한 많은 상담을 하려고 함

n = int(input())
work = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
# t, p 는 완료하는데 걸리는 기간 t, 상담을 했을 때 받을 수 있는 금액 p

# 0일차부터 n일차까지 벌 수 있는 돈
money = [0]*(n+1)

for i in range(1,n+1):
    time, pay = work[i]

    # 일을 했을 때, n일 전에 끝낼 수 있으면,
    if time + i <= n+1 :
        # 이전에 했던 일들 중에서,
        for j in range(i-1,-1,-1):
            # 일을 하고 나서, 일을 할 시간이 된다면, 금액을 추가
            if i >= work[j][0] + j:
                money[i] = max(money[j] + pay, money[i])

print(max(money))

