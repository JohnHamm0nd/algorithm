"""
재귀 호출을 사용하여 팩토리얼 출력하기
"""

def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)




if __name__ == "__main__":
    number = int(input("팩토리얼을 구할 수 입력 :"))
    print("%2d! = %20d"%(number,fact(number)))
