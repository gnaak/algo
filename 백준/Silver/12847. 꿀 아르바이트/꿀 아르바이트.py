# 꿀 아르바이트

# 1. 각 날마다 일의 차이때문에 일급이 다름
# 2. 일급을 당일에 넣어줌
# 3. 정해진 일 수 만큼만 일을 시킴
# 4. 한번이라도 퇴직하면, 다시 취직을 안시킴
#    단, 만약 취직을 한다면, 일을 시작한 날부터 끝날 때까지 빠지면 안된다

# 월세를 내기 바로 전날 까지인 n일과, 일을 할수 있는 날 m

n, m = map(int,input().split())
earn = list(map(int,input().split()))
stand = sum(earn[:m])
max_earn = stand
for i in range(m,n):
    stand += earn[i] - earn[i-m]
    max_earn = max(max_earn, stand)

print(max_earn)