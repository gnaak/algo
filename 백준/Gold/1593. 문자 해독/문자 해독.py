'''
백준 골드 5
문자 해독
'''

g, s = map(int,input().split()) # 단어 W의 길이 g, 추출한 문자열 S의 길이 s
W = str(input())
S = str(input())
wl = [0]*52
sl = [0]*52

for i in range(g):
    if ord(W[i]) >= 97:
        wl[ord(W[i])-71] +=1
    else:
        wl[ord(W[i])-65] +=1
cnt = 0
start = 0
length = 0

for i in range(s):
    if ord(S[i]) >= 97:
        sl[ord(S[i])-71] +=1
    else:
        sl[ord(S[i])-65] +=1
    length +=1
    if length == g :
        if wl == sl:
            cnt +=1
        if ord(S[start]) >= 97:  # 소문자
            sl[ord(S[start]) - 97 + 26] -= 1
        elif ord(S[start]) >= 65:  # 대문자
            sl[ord(S[start]) - 65] -= 1
        start+=1
        length-=1

print(cnt)