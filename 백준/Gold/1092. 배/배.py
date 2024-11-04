# 배
# 항구에는 크레인이 n대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
# 크레인은 무게 제한이 있다. 무게 제한 보다 무거운 박스는 옮길 수 없다. 최소 시간을 구하시오.

import sys
input = sys.stdin.readline

n = int(input()) # 크레인의 개수
cranes = list(map(int,input().split()))
m = int(input()) # 박스의 개수
boxes = list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
cannot = False
if cranes[0] < boxes[0]:
    cannot = True
else:
    while len(boxes) > 0:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue

            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1

print(time if not cannot else -1)
