## 전화번호 목록
## https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]

result = solution(phone_book)
print(result)