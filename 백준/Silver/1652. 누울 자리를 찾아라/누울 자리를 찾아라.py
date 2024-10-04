n = int(input().strip())

room = []
for _ in range(n):
    room.append(list(input().strip()))

answer = [0, 0]  # [가로로 누울 자리, 세로로 누울 자리]

for i in range(n):
    count_row = 0
    for j in range(n):
        if room[i][j] == '.':
            count_row += 1
        else:
            if count_row >= 2:
                answer[0] += 1
            count_row = 0
    if count_row >= 2:
        answer[0] += 1

    count_column = 0
    for j in range(n):
        if room[j][i] == '.':
            count_column += 1
        else:
            if count_column >= 2:
                answer[1] += 1
            count_column = 0
    if count_column >= 2:
        answer[1] += 1


print(*answer)