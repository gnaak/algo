n = int(input())

books = dict()

for _ in range(n):
    title = input().strip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

max_books = max(books.values())

answer = [title for title, cnt in books.items() if cnt == max_books]
answer.sort()

print(answer[0])