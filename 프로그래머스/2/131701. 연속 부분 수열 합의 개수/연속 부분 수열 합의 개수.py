def solution(elements):
    n = len(elements)
    answer = set()
    for i in range(len(elements)):
        sum = 0
        for j in range(i, n + i):
            sum += elements[j % n]
            answer.add(sum)
    return len(answer)