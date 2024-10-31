# 회사에 있는 사람

import sys
input = sys.stdin.readline


def check() :
    n = int(input())
    employee = dict()
    
    for _ in range(n):
        name, act = input().split()
        if act == 'enter':
            employee[name] = True  # 직원이 사무실에 있음을 표시
        else:
            if name in employee:
                del employee[name]  # 직원이 사무실을 나감
    
    # 이름을 역순으로 정렬하여 출력
    for name in sorted(employee.keys(), reverse=True):
        print(name)

check()