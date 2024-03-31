'''
백준 실버 5
영화감독 숌
'''

n = int(input())

cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt +=1
    if cnt == n:
        break
    result +=1

print(result)
