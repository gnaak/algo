'''
백준 브론즈 1
약수들의 합
'''

while True:
    n = int(input())
    if n == -1:
        break
    ans = []
    pri = []
    for i in range(1,n):
        if n % i == 0:
            ans.append(i)
    if sum(ans) == n:
        pri.append(str(n))
        pri.append(" = ")
        for an in ans:
            pri.append(str(an))
            pri.append(" + ")
        pri.pop()
        print(''.join(pri))
    else:
        print(n, end=" ")
        print("is NOT perfect.")