def card(n):
    if n == k:
        nums.append(''.join(temp))
        return

    for i in range(n1):
        if check[i] == 1:
            continue

        check[i] = 1
        temp.append(cards[i])
        card(n+1)
        check[i] = 0
        temp.pop()

n1 = int(input())
k = int(input())
cards = []
nums = []
temp = []
check = [0]*n1
for _ in range(n1):
    a = str(input())
    cards.append(a)

card(0)
print(len(set(nums)))
