"""
약수 구하기
"""

def divisor_number(number):
    for num in range(1, number+ 1):
        if number % num == 0:
            print("약수: %d" %(num))
        
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    divisor_number(number)
