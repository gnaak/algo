def solution(g, p):
    lst = {}
    g_lst = {}
    answer = []
    for i in range(len(g)):
        if g[i] not in lst:
            lst[g[i]] = 0
            g_lst[g[i]] = []
        lst[g[i]] += p[i]
        g_lst[g[i]].append((p[i],i))
    lst = sorted(lst.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in lst:
        print(genre)
        g_lst[genre].sort(key=lambda x: (-x[0], x[1]))

        for i in range(min(2,len(g_lst[genre]))):
            answer.append(g_lst[genre][i][1])
    return answer