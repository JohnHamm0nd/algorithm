"""
유클리드 호제법을 사용하여 최대공약수 구하기
"""

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)


if __name__ == "__main__":
    x, y =  list(map(int, input("최대 공약수를 구할 두 수을 입력하세요 : ").split()))
    print("{}와 {}의 최대공약수 : {}".format(x, y, gcd(x, y)))


"""
13, 14번 문제와 같은문제
"""
