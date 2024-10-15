# 방번호

# 다솜이는 은진이의 옆집에 새로 이사를 왔다
# 한 세트에는 0부터 9까지 숫자가 들어있다
# 6은 9를 뒤집을 수 있고, 9는 6을 뒤집을 수 있다

import sys
input = sys.stdin.readline

num_set = dict()
room_number = str(input().strip()) # n은 은진이의 방번호
for i in range(len(room_number)):
    if room_number[i] == '6' or room_number[i] == '9':
        if '69' in num_set:
            num_set['69'] += 1
        else:
            num_set['69'] = 1

    else:
        if room_number[i] in num_set:
            num_set[room_number[i]] += 1
        else:
            num_set[room_number[i]] = 1

if '69' in num_set :
    num_set['69'] = (num_set['69'] + 1) // 2

mx = max(num_set.values())
print(mx)