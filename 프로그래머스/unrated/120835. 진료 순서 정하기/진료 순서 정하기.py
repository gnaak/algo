def solution(emergency):
    answer=[]
    arr = sorted(emergency)
    for i in range(len(arr)):
        answer.append(len(arr)-emergency.index(arr[i]))
    return answer