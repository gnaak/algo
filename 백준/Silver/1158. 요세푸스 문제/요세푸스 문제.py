import sys
input = sys.stdin.readline

n, k = map(int, input().split())

have = [i for i in range(1, n + 1)]

m = 0
result = []
while have:
    m = (m + k - 1) % len(have)  # 현재 남은 사람의 수로 나눠서 인덱스 조정
    result.append(have.pop(m))   # 제거한 사람을 결과 리스트에 추가

print("<" + ", ".join(map(str, result)) + ">")
