# 회원 수 입력
n = int(input())

# 회원 정보 입력 및 등록 순서 추가
members = []
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

# 나이와 등록 순서를 동시에 고려한 정렬
members.sort(key=lambda x: (x[0], x[1]))

# 정렬된 회원 정보 출력
for member in members:
    print(member[0], member[2])
