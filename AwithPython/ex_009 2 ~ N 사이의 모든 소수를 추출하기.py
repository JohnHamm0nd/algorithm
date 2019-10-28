"""
2 ~ N 사이의 모든 소수를 추출하기
"""

def check_prime(number):
    for n in range(2, number + 1):
        num  = number + 1 // 2
        i = 2
        while i < num:
            if n % i == 0:
                break
            i += 1
        if i == n:
            print("%d" %n)
    
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    check_prime(number)
