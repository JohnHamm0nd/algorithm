"""
최소공배수 구하기
"""

def calc_LCM(x, y):
    i = 2
    while 1:
        if i % x == 0 and i % y == 0:
            break
        else:
            i += 1
    return i


if __name__ == "__main__":
    x, y =  list(map(int, input("최소공배수를 구할 두 수을 입력하세요 : ").split()))
    print("{}와 {}의 최소공배수 : {}".format(x, y, calc_LCM(x, y)))
