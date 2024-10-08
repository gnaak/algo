def can_transform(s, t):
    while len(t) > len(s):
        if t[-1] == 'A':
            t = t[:-1]  # 마지막 'A'를 제거
        elif t[-1] == 'B':
            t = t[:-1]  # 마지막 'B'를 제거하고
            t = t[::-1]  # 문자열을 뒤집음

    return s == t  # 변환 후 s와 t가 동일한지 확인

s = input().strip()
t = input().strip()

print(1 if can_transform(s, t) else 0)
