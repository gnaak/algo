def solution(array, commands):
    answer = []
    for command in commands:
        startidx, endidx, k = command
        startidx-=1
        endidx-=1
        k-=1
        answer.append(sorted(array[startidx:endidx+1])[k])
    return answer