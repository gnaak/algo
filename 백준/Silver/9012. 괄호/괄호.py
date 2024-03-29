n = int(input())
for _ in range(n):
    gwalho = input()
    queue = []
    for i in range(len(gwalho)):
        if gwalho[i] == '(':
            queue.append('(')
        else:
            if queue and queue[-1] == '(':
                queue.pop()
            else:
                print("NO")
                break  # 이 부분에서 바로 for 반복문을 빠져나갑니다.
    else:
        if len(queue) == 0:
            print("YES")
        else:
            print("NO")
