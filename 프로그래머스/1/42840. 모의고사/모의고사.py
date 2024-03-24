def solution(answers):
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == ans_1[i%len(ans_1)]:
            score[0]+=1
        if answers[i] == ans_2[i%len(ans_2)]:
            score[1]+=1
        if answers[i] == ans_3[i%len(ans_3)]:
            score[2]+=1
    max_scorer = max(score)
    winner = []
    for i in range(3):
        if score[i] == max_scorer:
            winner.append(i+1)
    return winner