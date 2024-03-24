def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    print(citations)
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h_index +=1
        else:
            break
    return h_index