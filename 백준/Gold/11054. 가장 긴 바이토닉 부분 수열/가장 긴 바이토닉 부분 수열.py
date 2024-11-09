n = int(input())
arr = list(map(int, input().split()))

# 증가하는 부분 수열
dp_inc = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

# 감소하는 부분 수열
dp_dec = [1] * n
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

# 바이토닉 수열의 최대 길이
result = 0
for i in range(n):
    result = max(result, dp_inc[i] + dp_dec[i] - 1)

print(result)
