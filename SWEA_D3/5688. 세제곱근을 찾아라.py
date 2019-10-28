"""
양의 정수 N에 대해 N = X3가 되는 양의 정수X 를 구하여라. 

[입력] 
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤1018) 이 주어진다.

[출력]
각 테스트 케이스마다 첫 번째 줄에는‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, N = X3가 되는 양의 정수 X를 출력한다. 
만약 이런 X가 존재하지 않으면 -1을 출력한다.
"""

import sys

sys.stdin = open('5688.txt', 'r', encoding = 'UTF-8')

for T in range(int(input())):
    number = int(input())
    a = round(pow(number, (1/3)), 3)
    b = int(a)
    if a == b:
        print('#%d %d' %(T+1, b))
    else:
        print('#%d %d' %(T+1, -1))
        
# round(N ** (1 / 3), 3) <- 세제곱근 a 구하는 다른방법(pow 함수 안쓰고 ** 제곱 사칙연산 으로 직접구함)
