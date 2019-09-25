"""
승현이는 N(2 ≤ N ≤ 10) 진법의 수 X(1 ≤ X ≤ N10,000,000) 를 공책에 적었다.
승현이는 손이 점점 아프기 시작했고, 머릿속에서 문득 X를 (N-1)로 나눈 나머지가 궁금해졌다.
승현이를 도와 N진법의 수 X가 주어졌을 때에 X를 (N-1)로 나눈 나머지를 계산하는 프로그램을 작성하라.
예를 들면, 9진법의 수 234는 10진법으로 193이고, 8로 나눈 나머지는 1이 된다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 정수 N, X가 공백 하나로 구분되어 주어진다.
X가 매우 큰 숫자임에 유의하라.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
N진법의 수 X가 주어졌을 때에 X를 (N-1)로 나눈 나머지를 출력한다.
"""

import sys

sys.stdin = open('7193.txt', 'r', encoding = 'UTF-8')


for T in range(int(input())):
    N, X = map(str, input().split())
    N = int(N)
    change_num = []
    for x in range(len(X)):
        change_num.append((N ** (len(X) - 1 - int(x))) * int(x))
    print('#%d %d' %(T+1, sum(change_num)//(N-1)))
