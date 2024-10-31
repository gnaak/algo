# 균형잡힌 세상

import sys
input = sys.stdin.readline

while 1 :
    stack = []
    isFlag = True
    sen = str(input())
    if sen[0] == '.':
        break

    for w in sen:
        if w == '(' or w == '[':
            stack.append(w)
        elif w == ')':
            if not stack or stack.pop() != '(':
                isFlag = False
                break
        elif w == ']':
            if not stack or stack.pop() != '[':
                isFlag = False
                break
        elif w == '.':
            break
    if isFlag and not stack:
        print('yes')
    else:
        print('no')