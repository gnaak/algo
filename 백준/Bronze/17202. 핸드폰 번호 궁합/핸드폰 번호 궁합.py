'''
백준 브론즈 1
핸드폰 번호 궁합
'''

ans = []
num1 = str(input())
num2 = str(input())
for i in range(len(num1)):
    ans.append(num1[i])
    ans.append(num2[i])

while len(ans) > 2 :
    for i in range(len(ans)-1):
        plus = int(ans[i]) + int(ans[i+1])
        if plus >= 10:
            ans[i] = plus-10
        else:
            ans[i] = plus
        if i == len(ans)-2:
            ans.pop()
for an in ans:
    print(an, end="")