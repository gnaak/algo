import sys
input = sys.stdin.readline

n = int(input().strip())
files = [input().strip() for _ in range(n)]

answer = ''
if n == 1:
    answer = files[0]
else:
    for i in range(len(files[0])):  # 모든 파일의 길이는 같음
        same_char = files[0][i]
        for j in range(1, n):
            if files[j][i] != same_char:
                answer += '?'
                break
        else:
            answer += same_char

print(answer)
