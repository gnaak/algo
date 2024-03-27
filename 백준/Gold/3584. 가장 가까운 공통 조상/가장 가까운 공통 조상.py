'''
백준 골드 4
가까운 조상 찾기
'''

tc= int(input())
for _ in range(tc):
    n = int(input())
    parent_node = [0 for _ in range(n+1)] # 부모 노드 저장용
    for i in range(n-1):
        p, c = map(int,input().split())
        parent_node[c] = p  #

    a, b = map(int,input().split())
    a_parent = [a]
    b_parent = [b]

    while parent_node[a]:
        a_parent.append(parent_node[a])
        a=parent_node[a]

    while parent_node[b]:
        b_parent.append(parent_node[b])
        b=parent_node[b]

    a_level = len(a_parent)-1
    b_level = len(b_parent)-1

    while a_parent[a_level] == b_parent[b_level]:
        a_level -=1
        b_level -=1
    print(a_parent[a_level+1])
