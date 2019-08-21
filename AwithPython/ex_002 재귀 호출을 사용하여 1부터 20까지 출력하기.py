"""
재귀 호출을 사용하여 1부터 20까지 출력하기
"""


def print_number(number):
    if number < 1:
        pass
    else:
        print_number(number-1)
        print(number)
 
        
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print_number(number)
