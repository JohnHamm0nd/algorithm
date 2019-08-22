"""
반복문을 사용하여 최대공약수 구하기
유클리드 호제법 사용
"""

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        z = y
        y = x % y
        x = z
    return z

if __name__ == "__main__":
    x, y =  list(map(int, input("최대 공약수를 구할 두 수을 입력하세요 : ").split()))
    print("{}와 {}의 최대공약수 : {}".format(x, y, gcd(x, y)))

"""
유클리드 호제법은 큰 수에서 작은 수를 나누어 나머지가 0이 되면 최대공약수, 나머지가 있을 경우 작은 수를 큰 수로 놓고 나머지를 작은 수로 놓아 다시 나누기를 반복, 
반복문을 사용하기 위하여 작은 수를 담아둘 변수를 하나 만들어 사용(그렇지 않으면 작은 수가 변경 되어 구하기 어려움)
"""
