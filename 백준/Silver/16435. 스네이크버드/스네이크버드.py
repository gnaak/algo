n, l = map(int,input().split())
food = list(map(int,input().split()))
food.sort()

end = 0
length = l
while end < n and food[end] <=length:
    length += 1
    end += 1

print(length)