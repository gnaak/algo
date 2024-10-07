# 팰린드롬인 문자열로 바꾸기
# 정답이 여러가지인 경우에는 사전 순으로
# 팰린드롬이 안되는 경우에는 -1

import sys
input = sys.stdin.readline

ans_lst = []
count = dict()
word = input().strip()

for a in word:
    if a in count:
        count[a] +=1
    else:
        count[a] = 1


odd_char = []
for char, cnt in count.items():
    if cnt % 2 != 0 :
        odd_char.append(char)

if len(odd_char) > 1: # 홀수 개수가 1개가 넘어가면 팰린드롬을 만들 수 없음
    print("I'm Sorry Hansoo")
else:
    ans = []
    left = []
    middle = ""

    for char in sorted(count.keys()):
        cnt = count[char]
        if cnt%2 != 0:
            middle = char
        left.append(char*(cnt//2))

    print(''.join(left) + middle + ''.join(left[::-1]))

