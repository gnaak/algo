# 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.
# 프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다.
# 각 종의 이름을 사전 순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지
import sys 
input = sys.stdin.readline

tree_dict = {}
while True:
    tree = input().strip()
    if tree == "":
        break

    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1


tot_trees = sum(tree_dict.values())
for tree in sorted(tree_dict.keys()):
    percentage = tree_dict[tree]/tot_trees*100
    print(f'{tree} {percentage:.4f}')