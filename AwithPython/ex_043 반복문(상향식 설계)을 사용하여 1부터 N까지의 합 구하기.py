"""
반복문(상향식 설계)을 사용하여 1부터 N까지의 합 구하기
"""

def sum_number(number):
    sum_num = 0
    while number > 0:
        sum_num += number
        number -= 1
    return sum_num
        

if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print(sum_number(number))
    
"""
재귀호출을 사용하지 않는다는 것 빼고는 이미 42번에서 사용하여 푼듯
"""
