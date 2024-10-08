# DNA란 어떤 유전물질을 구성하는 분자
# A, T, G, C로 구성되어 있다
# Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수

import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # n개의 dna, 길이 m
dnas = list(str(input().strip()) for _ in range(n))

ans = ""
ans_cnt = 0
for i in range(m):
    dna_dict = {"A":0,"C":0,"G":0,"T":0}

    for dna in dnas:
        if dna[i] == 'A':
            dna_dict["A"] += 1
        if dna[i] == 'C':
            dna_dict["C"] += 1
        if dna[i] == 'G':
            dna_dict["G"] += 1
        if dna[i] == 'T':
            dna_dict["T"] += 1

    max_cnt = 0
    character = ""
    for char, cnt in dna_dict.items():
        if cnt > max_cnt:
            max_cnt = cnt
            character = char
    ans_cnt += n - max_cnt
    ans += character

print(ans)
print(ans_cnt)