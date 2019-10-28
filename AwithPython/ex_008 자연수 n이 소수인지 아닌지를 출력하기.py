"""
자연수 n이 소수인지 아닌지를 출력하기
"""

def check_prime(number):
    n  = number + 1 // 2
    i = 2
    while i < n:
        if number % i == 0:
            print("%d는 합성수 입니다." %number)
            break
        i += 1
    if i == n:
        print("%d는 소수 입니다." %number)
    
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    check_prime(number)
