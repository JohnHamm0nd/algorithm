"""
동적 계획법을 사용하여 1부터 N까지의 합 구하기(재귀 호출 사용)
"""

def sum_number(number):
    while number <= 0:
        return 0
    return number + sum_number(number - 1)

if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print(sum_number(number))
