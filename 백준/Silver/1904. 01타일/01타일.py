def count_num(N) :
    MOD = 15746
    
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    arr = [0] * (N+1)

    arr[1] = 1
    arr[2] = 2

    for i in range(3,N+1):
        arr[i] = (arr[i-1] + arr[i-2]) % MOD
    
    return arr[N]

N = int(input())
print(count_num(N))