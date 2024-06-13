import sys
input = sys.stdin.readline

s = str(input().strip())

words = set()
for i in range(len(s)): # 자르기 시작할 위치
    for j in range(1,len(s)-i+1): # 최소 1개, 최대 길이는 i부터 끝까지
        words.add(s[i:j+i])

print(len(words)
      )


