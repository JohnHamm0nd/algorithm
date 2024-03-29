"""
두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

[제약 사항]

1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)
2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.

[입력]
입력으로 두 개의 자연수 a, b가 빈 칸을 두고 주어진다.

[출력]
사칙연산의 결과를 각 줄에 순서대로 출력한다.
"""

import sys
sys.stdin = open('1938.txt', 'r')

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)

"""
다른답안
x = input().split()
a, b = int(x[0]), int(x[-1])

print(f'{a+b}\n{a-b}\n{a*b}\n{round(a/b)}')
"""
