def solution(priorities, location):
    queue = []
    answer= 0
    for idx in range(len(priorities)):
        queue.append((priorities[idx],idx))
    
    while queue:
        current = queue.pop(0)
        is_higher = False
        for p in queue:
            if current[0]<p[0]:
                is_higher = True
                break
        if is_higher:
            queue.append(current)
        else:
            answer+=1
            if current[1] == location:
                return answer
    return answer