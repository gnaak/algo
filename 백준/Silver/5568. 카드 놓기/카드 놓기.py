

def making(N):
    if N == k:
        result.append(''.join(temp))
        return

    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            temp.append(cards[i])
            making(N+1)
            temp.pop()
            check[i]=0

n = int(input())
k = int(input())
cards = []
result = []
temp = []
check = [0]*n
for _ in range(n):
    cards.append(str(input()))

making(0)
print(len(set(result)))
