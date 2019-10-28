"""
반복문을 상요하여 피보나치 수열 구하기
"""

def fib(number):
    a = 1
    b = 1
    for n in range(1, number + 1):
        if n < 3:
            print("피보나치 %2d = %10d"%(n,a))
        else:
            c = a+ b
            a = b
            b = c
            print("피보나치 %2d = %10d"%(n,c))


if __name__ == "__main__":
    number = int(input("구하려는 피보나치 수열의 수를 입력하세요. : "))
    fib(number)

