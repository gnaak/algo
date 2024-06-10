def solution(s):
    p = s.split(' ')
    answer = p[0]
    a = int(answer)
    for i in range(len(p)):
        if p[i] == '+':
            a += int(p[i+1])
        elif p[i] == '-':
            a -= int(p[i+1])
    return a