import sys
input = sys.stdin.readline

line = str(input().strip())
line_list = list(line)

for i in range((len(line))-1):
    if line_list[i] == line_list[i+1]:
        line_list[i] = "*"

print(min(line_list.count("0"), line_list.count("1") ))