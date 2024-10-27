import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    p = input().strip()  # 수행할 함수
    n = int(input())  # 배열 내 원소 개수
    xs = input().strip()[1:-1]  # 배열 부분을 추출
    nums = xs.split(',') if xs else []  # 빈 배열 처리

    is_reversed = False
    error_occurred = False

    for op in p:
        if op == 'R':
            is_reversed = not is_reversed  # 뒤집기 상태 토글
        elif op == 'D':
            if nums:
                if is_reversed:
                    nums.pop()  # 뒤집힌 경우는 끝에서 제거
                else:
                    nums.pop(0)  # 정방향일 때는 앞에서 제거
            else:
                print("error")
                error_occurred = True
                break

    if not error_occurred:
        if is_reversed:
            nums.reverse()
        print("[" + ",".join(nums) + "]")
