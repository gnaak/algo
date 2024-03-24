def solution(brown, yellow):
    total = brown + yellow
    answer = []
    
    for x in range(1,int(yellow**0.5)+1):
        if yellow % x == 0:
            y = yellow //x 
            if 2*(x+y+2) == brown:
                answer.append(y+2)

                answer.append(x+2)
        
    return answer