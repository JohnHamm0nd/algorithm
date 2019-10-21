"""
다음은 233 이란 10진수를 2진수로 변환하는 과정을 나타낸 그림이다.

위 그림을 참조하여 라이브러리를 사용하지 말고 10진수를 n진수로 변환하는 프로그램을 작성하시오.. (단, n의 범위는 2 <= n <= 16)

예)
2진수로 변환 : 233,10 --> 11101001,2
8진수로 변환 : 233,10 --> 351,8
16진수로 변환 : 233,10 --> E9,16
"""

X, Y = map(int, input('X(10진수) 와 Y(변환할 진수) 입력: ').split())
stack = []
change_list = '0123456789ABCDEF'
while X // Y:
    stack.append(change_list[X%Y])
    X = X // Y
stack.append(change_list[X])
print(''.join(map(str, reversed(stack))), Y)


"""
# 다른 방법
# 재귀함수와 divmod 함수 사용
# 더 좋은 방법인지는 모르겠다.

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


print(convert(233, 2))
print(convert(233, 8))
print(convert(233, 16))
"""
