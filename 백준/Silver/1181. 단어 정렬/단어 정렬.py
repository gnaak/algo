# 알파벳 소문자가 들어오면 1. 길이가 짧은 순서, 길이가 같다면 사전 순으로

import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input())

set_lst = set(words)
word_lst = list(set_lst)
word_lst.sort()
word_lst.sort(key=len)

for word in word_lst:
    print(word, end = '')