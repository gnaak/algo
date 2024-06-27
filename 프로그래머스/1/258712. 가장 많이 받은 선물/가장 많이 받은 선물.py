def solution(friends, gifts):
    gift_s = {friend : [] for friend in friends}
    gift_r = {friend : 0 for friend in friends}
    for gift in gifts:
        s, r = gift.split()
        gift_s[s] = []

    for gift in gifts:
        s, r = gift.split()
        gift_r[s] += 1
        gift_r[r] -= 1
        gift_s[s].append(r)

    n = len(friends)
    graph = [[0]*(n) for _ in range(n)]
    hashed_friend = {friends[i]: i for i in range(n)} 
    
    # 그래프 만들기 
    for sender in gift_s:
        for reciever in gift_s[sender]:
            graph[hashed_friend[sender]][hashed_friend[reciever]] += 1 
    
    answer = 0
    gift = [0]*n
    for i in range(n):
        for j in range(n):
            if i != j:
                if graph[i][j] != graph[j][i]:
                    if graph[i][j] > graph[j][i]:
                        gift[i] += 1
                else: 
                    if gift_r[friends[i]] != gift_r[friends[j]]:
                        if gift_r[friends[i]] > gift_r[friends[j]]: 
                            gift[i] += 1
    return max(gift)
