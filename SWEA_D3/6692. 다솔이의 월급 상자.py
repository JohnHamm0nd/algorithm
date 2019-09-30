"""
다솔이가 다니는 회사는 이번 달부터 월급을 상자에 담아 주기로 했다.
이 상자에는 Pi의 확률로 Xi만원이 들어 있다.
다솔이가 받을 수 있는 월급의 평균은 얼마인지 구해보자.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(2<=N<=20)이 주어진다.
다음 N개의 줄의 번째 줄에는 하나의 실수 Pi(0<Pi<=1)과 하나의 정수 Xi(1<=<Xi<=100000)가 공백으로 구분되어 주어진다.
Pi는 소수점 이하 여섯 자리까지의 수를 가질 수 있다. Pi의 총합은 1이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후, 한 줄에 다솔이가 얻을 수 있는 월급의 평균을 출력한다.
정답과의 절대오차 혹은 상대 오차가 10^(-6)이하이면 정답으로 인정된다.
"""


import sys

sys.stdin = open('6692.txt', 'r', encoding = 'UTF-8')

"""
for T in range(int(input())):
    N = int(input())
    salaries = []
    for n in range(N):
        P, X = map(float, input().split())
        salaries.append(P * X)
    print('#%d %f' %(T+1, sum(salaries)))
# 실행시간 401ms ( 테스트케이스 1000개 )
"""

results = []
for T in range(int(input())):
    N = int(input())
    salaries = []
    for n in range(N):
        P, X = map(float, input().split())
        salaries.append(P * X)
    results.append(sum(salaries))
for i, r in enumerate(results):
    print('#%d %f' %(i+1, r))
# 실행시간 288ms ( 테스트케이스 1000개 )
