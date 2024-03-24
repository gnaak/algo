def solution(phone_book):
    phone_book.sort()  # 전화번호를 사전순으로 정렬하여 비교를 쉽게 함
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True
