"""
1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.
참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

[입력]
이 문제의 입력은 없다.

[출력]
1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.
"""

"""
for n in range(2, 100001):
    i = 2
    while i < 100001:
        if n % i == 0:
            break
        i += 1
    if i == n:
        print(n, end = " ")
#제한시간 초과
"""

TRUE = 1
FALSE = 0

def calc_prime(number):
    check = [TRUE] * number 
    check[0] = FALSE
    check[1] = FALSE
    i = 2
    while i < number:
        j = 2
        while i*j < number:
            check[i*j] = FALSE
            j = j + 1
        i = i + 1
    for i in range(0, len(check)):
        if check[i] == TRUE:
            print(i, end = " ")

calc_prime(100001)

# 아리토스테네스의 체
# 첫번째 방법과 많은 속도 차이가 난다
