"""
반복문을 사용하여 팩토리얼 출력하기
"""

def fact(number):
    ans = 1
    for n in range(1, number + 1):
        ans *= n
    return ans

if __name__ == "__main__":
    number = int(input("팩토리얼을 구할 수 입력 :"))
    print("%2d! = %20d"%(number,fact(number)))
