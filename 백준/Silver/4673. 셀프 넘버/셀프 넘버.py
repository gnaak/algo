# 셀프 넘버

# 생성자가 없는 숫자를 셀프 넘버라고 한다
# 모든 수를 돌면서 셀프넘버를 확인해본다?

self = [0]*10001

for num in range(1,10001):
    ans = num

    while num > 0:
        ans += num % 10
        num //= 10
    if ans < 10001 and ans != num:
        self[ans] = 1

for i in range(1,10001):
    if self[i] == 0 :
        print(i)