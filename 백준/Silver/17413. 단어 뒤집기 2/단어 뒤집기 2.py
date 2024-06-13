import sys
input = sys.stdin.readline

s = str(input().strip())

# s는 알파벳 소문자, 숫자, 공백, 특수 문자
# 시작과 끝은 공백이 아니다
# '<'로 시작해 '>'로 끝나는 부분은 태그이며, 태그는 단어가 아니다 == 뒤집지 않는다
# 태그와 단어 사이에는 공백이 없다
answer = ''

word = '' # 단어
isTag = 0 # 태그 여부
for i in range(len(s)): # 문자 전체 길이에 대해서
    if s[i] == ' ': # 공백이 오면,
        answer += word[::-1]
        answer += ' '
        word = ''
    elif s[i] == '<':
        isTag = 1 # 태그 열림 표시
        answer += word[::-1] # 태그 열기 전에 앞에 글자가 있으면 추가
        answer += s[i]
        word = ''
    elif s[i] == '>':
        isTag = 0 # 태그 닫힘 표시
        answer += s[i]
    else: # 알파벳 소문자
        if isTag: # 태그 안에 있는 소문자면, 그냥 집어넣어줌
            answer += s[i]
        else:
            word += s[i]
            if i == len(s)-1 : # 마지막 글자면,
                answer += word[::-1] # 값 추가

print(answer)


