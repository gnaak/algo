n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
money = [0] * (n + 1)  # n+1 크기의 DP 테이블

for i in range(n):
    time, pay = work[i]
    # 현재 날짜까지의 최대 수익을 다음 날들에 반영
    if i + time <= n:  # 퇴사일을 넘지 않으면
        money[i + time] = max(money[i + time], money[i] + pay)
    # 다음 날의 최대 수익도 현재까지의 최대 수익으로 갱신
    money[i + 1] = max(money[i + 1], money[i])

print(money[n])
