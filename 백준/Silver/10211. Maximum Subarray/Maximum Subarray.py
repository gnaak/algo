import sys

input = sys.stdin.readline


def max_subarray():
    n = int(input())
    arr = list(map(int, input().split()))

    current_sum = max_sum = arr[0]
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    print(max_sum)


# 테스트 케이스 실행
tc = int(input())
for _ in range(tc):
    max_subarray()
