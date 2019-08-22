"""
약수의 합 출력하기
"""

def sum_divisor_number(number):
    sum_number = 0
    for num in range(1, number+ 1):
        if number % num == 0:
            sum_number += num
    print("약수의 합: %d" %(sum_number))
        
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    sum_divisor_number(number)
