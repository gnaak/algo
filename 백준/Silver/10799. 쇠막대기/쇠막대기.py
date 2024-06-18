import sys
input = sys.stdin.readline

n = input().strip()
stk = 0 # 현재 쇠막대기의 갯수
ans = 0 # 나눠진 쇠막대기의 개수
for i in range(len(n)): # 스틱과 레이저를 도는 동안;
    if n[i] == '(':
        if n[i+1] == '(': # 쇠막대기 += 1
            stk += 1
        else: # ')' 이면 레이저
            ans += stk # 쇠막대기 개수만큼 한개씩 더 늘어남
    else: # ')' 인 경우에 0은 무조건 (로 시작?
        if n[i-1] == ')': # 레이저가 닫힌게 아니면,
            stk -=1 # 쇠막대기 끝
            ans +=1 # 쇠막대기 끝나면서 한 조각 추가

print(ans)