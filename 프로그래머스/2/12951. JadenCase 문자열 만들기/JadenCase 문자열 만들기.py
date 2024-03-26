def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        if word != "":
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append("")
        
    return (' ').join(answer)