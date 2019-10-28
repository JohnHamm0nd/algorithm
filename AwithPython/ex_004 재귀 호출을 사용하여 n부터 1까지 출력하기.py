"""
재귀 호출을 사용하여 n부터 1까지 출력하기
"""

def print_number(number):
    if number > 0:
        print(number)
        print_number(number - 1)
        
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print_number(number)
