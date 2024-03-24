def solution(progresses, speeds):
    answer = []
    queue = []

    # 각 작업이 완료되는데 걸리는 일수를 계산하여 큐에 저장
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        days = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            days += 1
        queue.append(days)

    # 첫 번째 기능부터 배포되는 기능 수 계산
    cnt = 1
    front = queue.pop(0)
    while queue:
        if front >= queue[0]:
            cnt += 1
            queue.pop(0)
        else:
            answer.append(cnt)
            cnt = 1
            front = queue.pop(0)
    answer.append(cnt)

    return answer
