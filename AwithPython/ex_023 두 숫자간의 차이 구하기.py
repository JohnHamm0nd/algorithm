"""
두 숫자간의 차이 구하기
"""

def cha_abs(a, b):
    if a > b:
        return a-b
    else:
        return b-a

if __name__ == "__main__":
    a, b =  list(map(int, input("차이를 구할 두 수을 입력하세요 : ").split()))
    print("{}와 {} 두 숫자간의 차이는 : {}".format(a, b, abs(a-b)))
    print("{}와 {} 두 숫자간의 차이는 : {}".format(a, b, cha_abs(a, b)))
