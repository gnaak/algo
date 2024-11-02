# 소가 길을 건너간 이유 1

# 존은 소의 위치를 n번 관찰
# 각 관찰은 소의 번호, 소의 위치
# 소의 번호는 1~10이고, 길의 왼쪽과 오른쪽을 뜻하는 0, 1

# 소가 최소 몇번 건넜는지 확인

n = int(input())
cows = dict()
cnt = 0
for _ in range(n):
    cow, place = input().split()
    if cow in cows and cows[cow] != place:
        cnt += 1
    cows[cow] = place


print(cnt)