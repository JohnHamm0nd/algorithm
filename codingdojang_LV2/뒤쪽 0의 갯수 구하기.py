"""
N!의 정의는 다음과 같습니다.

N! = 1 * 2 * 3 * 4 ... N
이때 N!를 정수로 변환 해 뒤에서 부터 연속되는 0의 갯수를 구하세요.

예) f(12) -> 2 # 12!은 479001600 f(25) -> 6 # 25!은 15511210043330985984000000

출처: codewars
"""

def factorial(N):
    fac = 1
    while N > 1:
        fac *= N
        N -= 1
    return fac

def check_0(N):
    count = 0
    i = 0
    N = ''.join(reversed(str(N)))
    while N[i] == '0':
        count += 1
        i += 1
    return count
    
N = int(input())
print(check_0(factorial(N)))
