"""
반복문을 사용하여 1부터 n까지 출력하기
"""

def print_number(number):
    for n in range(1, number + 1):
        print(n)
        
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print_number(number)
