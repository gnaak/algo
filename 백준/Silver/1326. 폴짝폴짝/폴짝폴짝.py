
def bfs():
    queue = [a-1]
    visited = [-1] * n
    visited[a-1] = 0

    while queue:
        current = queue.pop(0)

        for i in range(current, n, node[current]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[current] + 1
                if i == b - 1:
                    return visited[i]

        for i in range(current, -1, -node[current]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[current] + 1
                if i == b - 1:
                    return visited[i]

    return -1


n = int(input())
node = list(map(int,input().split()))
a , b = map(int,input().split())
print(bfs())