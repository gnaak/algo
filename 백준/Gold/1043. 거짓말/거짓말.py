import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truthy = list(map(int, input().strip().split()))
truth = set(truthy[1:]) if truthy[0] > 0 else set()  # 진실을 아는 사람들 집합
parties = []

# 각 파티 정보 저장
for _ in range(m):
    party = list(map(int, input().strip().split()))
    parties.append(party[1:])

# 진실을 아는 사람 집합을 확장하는 과정 반복
changed = True
while changed:
    changed = False
    for party in parties:
        # 파티 구성원 중에 진실을 아는 사람이 있으면 전체를 진실 집합에 추가
        if truth.intersection(party):
            before_update_size = len(truth)
            truth.update(party)
            if len(truth) > before_update_size:  # 집합이 확장되었으면 다시 반복
                changed = True

# 거짓말을 할 수 있는 파티 수 계산
lied_party_count = 0
for party in parties:
    if not truth.intersection(party):  # 진실을 아는 사람이 없으면 거짓말 가능
        lied_party_count += 1

print(lied_party_count)
