from collections import deque
def solution(elements):
    queue = deque(elements)
    answer = set()
    for i in range(len(elements)):
        sum = 0
        for e in queue:
            sum += e
            answer.add(sum)
        queue.rotate()
    
    return len(answer)