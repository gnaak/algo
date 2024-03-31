'''
백준 브론즈 1
부녀회장이 될테야!
'''

tc = int(input())
for _ in range(tc):
    k = int(input())
    n = int(input())
    apt = [[0]*15 for _ in range(15)]
    for i in range(1,15):
        apt[0][i] = i
        apt[i][1] = 1

    for i in range(1,k+1):
        for j in range(1,n+1):
            apt[i][j] = apt[i][j-1]+apt[i-1][j]

    print(apt[k][n])
