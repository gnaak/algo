'''
백준 실버 5
파스칼의 삼각형
'''

n, k = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
arr[0][0] = 1
for i in range(n+1):
    arr[i][0] = 1
    arr[i][i] = 1
    for j in range(1,i):
        arr[i][j] = arr[i-1][j]+arr[i-1][j-1]
print(arr[n-1][k-1])