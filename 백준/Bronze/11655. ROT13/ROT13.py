import sys
input = sys.stdin.readline

s = input()
answer = ""

for i in range(len(s)):
    if s[i].isalpha():  # 알파벳 문자인지 확인
        # 대문자와 소문자를 구분하여 처리
        if s[i].isupper():
            answer += chr((ord(s[i]) - ord('A') + 13) % 26 + ord('A'))
        else:
            answer += chr((ord(s[i]) - ord('a') + 13) % 26 + ord('a'))
    else:
        answer += s[i]  # 알파벳 문자가 아니면 그대로 추가

print(answer)  # 결과 출력