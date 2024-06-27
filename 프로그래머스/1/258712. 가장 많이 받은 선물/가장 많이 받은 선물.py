def solution(friends, gifts):
    n = len(friends)
    gift_lst = {}
    gift_zisu = {friend : 0 for friend in friends}
    for i in range(n):
        gift_lst[friends[i]] = i
    
    graph =[[0]*n for _ in range(n)]
    
    for gift in gifts:
        send, recieve = gift.split(" ")
        graph[gift_lst[send]][gift_lst[recieve]]+=1
        gift_zisu[send] += 1
        gift_zisu[recieve] -= 1
    answer = [0]*n
    for i in range(n):
        for j in range(n):
            if i != j :
                if graph[i][j] > graph[j][i]:
                    answer[i] +=1 
                    
                elif graph[i][j] == graph[j][i]:
                    if gift_zisu[friends[i]] > gift_zisu[friends[j]]:
                        answer[i] += 1

    return max(answer)
                    