tc = int(input())
for _ in range(tc):
    n = int(input())
    parent_node = [0 for i in range(n+1)]
    for i in range(n-1):
        p, c = map(int,input().split())
        parent_node[c] = p

    a, b = map(int,input().split())
    a_anc = [a]
    b_anc = [b]

    while parent_node[a]:
        a = parent_node[a]
        a_anc.append(a)

    while parent_node[b]:
        b = parent_node[b]
        b_anc.append(b)
    a_lv = len(a_anc)-1
    b_lv = len(b_anc)-1
    while a_anc[a_lv] == b_anc[b_lv]:
        a_lv -=1
        b_lv -=1

    print(a_anc[a_lv+1])
