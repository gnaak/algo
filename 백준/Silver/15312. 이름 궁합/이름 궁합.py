'''
백준 실버 5
이름 궁합
'''

al = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
ls = []
my = str(input())
her = str(input())
for i in range(len(my)):
    ls.append(al[ord(my[i])-65])
    ls.append(al[ord(her[i])-65])

while len(ls) > 2 :
    for i in range(len(ls)-1):
        ls[i] = (ls[i]+ls[i+1])%10
    ls.pop()
for l in ls:
    print(l,end="")