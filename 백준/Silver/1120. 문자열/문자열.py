import sys
input = sys.stdin.readline

a, b = map(str, input().split())

# 특수한 경우를 제거하고 단순 비교로만 진행
if len(a) == len(b):  # 길이가 같은 경우 바로 비교
    ans = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    print(ans)
else:  # a의 길이가 더 작은 경우
    answer = len(a)  # 최대값으로 초기화 (a의 길이만큼 다를 수 있음)
    for i in range(len(b) - len(a) + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] != b[j + i]:
                cnt += 1
        answer = min(answer, cnt)
    print(answer)
