"""
소인수분해 구하기
"""

def calc_prime_factorization(number):
    for i in range(2, number + 1):
        while 1:
            if number % i == 0:
                number = number // i
                print(i, end = " ")
            else:
                break




if __name__ == "__main__":
    number = int(input("소인수분해 할 수를 입력하세요. : "))
    calc_prime_factorization(number)
