"""
3과 5의 배수 계산하기
"""

def check_common(number):
    for n in range(1, number + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("%d는 3과 5의 공배수 입니다." %n)
            
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    check_common(number)
