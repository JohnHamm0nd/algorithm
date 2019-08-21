"""
숫자 뒤집기
"""

def reverse_number(number):
    if number == 0:
        return 0
    print(number % 10, end = "")
    reverse_number(number // 10)



if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    reverse_number(number)
