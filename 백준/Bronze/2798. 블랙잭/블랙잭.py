'''
백준 브론즈 2
블랙잭
'''

n, m = map(int,input().split())
cards = list(map(int,input().split()))

max_card = 0 
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = cards[i] + cards[j] + cards[k]
            if total >= max_card and total <= m:
                max_card = total
print(max_card)