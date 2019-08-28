"""
제곱근 구하기
"""

def mysqrt(number):
    sqrt_count = 0
    sqrt_number = 1
    while number >= 0:
        number -= sqrt_number
        sqrt_number += 2
        sqrt_count += 1
    return sqrt_count - 1

if __name__ == "__main__":
    number = int(input("제곱근을 구할 수 입력 :"))
    print("%2d의 제곱근은 %2d"%(number,mysqrt(number)))
