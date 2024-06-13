n = int(input().strip())

room = []
for _ in range(n):
    room.append(list(input().strip()))

answer = [0, 0]  # [가로로 누울 자리, 세로로 누울 자리]

# 가로로 누울 자리 카운트
for i in range(n):
    count = 0
    for j in range(n):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                answer[0] += 1
            count = 0
    if count >= 2:
        answer[0] += 1

# 세로로 누울 자리 카운트
for i in range(n):
    count = 0
    for j in range(n):
        if room[j][i] == '.':
            count += 1
        else:
            if count >= 2:
                answer[1] += 1
            count = 0
    if count >= 2:
        answer[1] += 1

print(*answer)
