g, s = map(int,input().split())
w = str(input())
S = str(input())

w_l = [0]*58
s_l = [0]*58
start= 0
length= 0
cnt = 0
for i in range(g):
    w_l[ord(w[i])-65] +=1

for i in range(s):
    s_l[ord(S[i])-65] +=1
    length +=1
    if length == g:
        if w_l == s_l:
            cnt +=1

        s_l[ord(S[start])-65]-=1
        start+=1
        length-=1
print(cnt)

