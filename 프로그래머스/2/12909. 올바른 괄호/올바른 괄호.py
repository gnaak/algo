def solution(s):
    queue = []
    for i in range(len(s)):
        if s[i] == '(':
            queue.append('(')
        else:
            if not queue or queue.pop() !='(':
                return False
    
    if len(queue) != 0:
        return False
    return True