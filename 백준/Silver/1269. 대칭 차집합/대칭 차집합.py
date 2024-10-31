import sys
input = sys.stdin.readline


def check() :
    n, m = map(int,input().split())
    a_lst = input().strip().split()
    b_lst = input().strip().split()
    tot_lst = a_lst + b_lst
    set_tot_lst = set(tot_lst)
    cmm = n + m - len(set_tot_lst)
    print(n + m - 2*cmm)


check()