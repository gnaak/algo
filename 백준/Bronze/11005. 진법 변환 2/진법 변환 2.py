arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
a, b = map(int,input().split())
while a :
    c = a%b
    ans+=arr[a%b]
    a //= b

print(ans[::-1])
