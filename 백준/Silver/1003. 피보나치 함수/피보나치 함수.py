tc = int(input()) # tc 개수
for _ in range(tc):
    n = int(input())

    a, b = 1, 0  # 0과 1이 호출된 횟수
    for i in range(n):
        # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        a, b = b, a + b
    print(a, b)
