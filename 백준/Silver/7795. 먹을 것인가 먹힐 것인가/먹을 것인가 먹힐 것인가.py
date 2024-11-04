# 먹을 것인가 먹힐 것인가

# A는 B를 먹는다
# A는 자기보다 작은 먹이만 먹을 수 있다.

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    cnt = 0

    for a_fish in a:
        start = 0  # b의 시작 포인터를 여기서 초기화
        while start < m and a_fish > b[start]:  # a_fish가 b[start]보다 크면
            cnt += 1
            start += 1  # 다음 b의 물고기로 넘어감

    print(cnt)