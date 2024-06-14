import sys
input = sys.stdin.readline

n = int(input())
target = set(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))
for num in nums:
    if num in target:
        print(1)
    else:
        print(0)
        