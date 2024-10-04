import sys
input = sys.stdin.readline

n = int(input())
book_lst = dict()
for _ in range(n):
    book = input()
    if book in book_lst:
        book_lst[book] += 1
    else:
        book_lst[book] = 1

ans_lst = []
max_cnt = max(book_lst.values())
for book, cnt in book_lst.items():
    if cnt == max_cnt:
        ans_lst.append(book)
ans_lst.sort()
print(ans_lst[0])