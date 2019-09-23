"""
양의 정수가 주어질 때, 이 수가 홀수인지 짝수인지 판별하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 100자리 이하의 양의 정수가 주어진다.

[출력]
각 테스트 케이스마다 첫 번째 줄에는‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, 주어진 수가 홀수이면 “Odd”를, 짝수이면 “Even”을 출력한다.
"""

import sys

sys.stdin = open('5549.txt', 'r', encoding = 'UTF-8')

results = []
for T in range(int(input())):
    number = input()
    number = int(number[-1])
    if number % 2 == 1:
        results.append('Odd')
    else:
        results.append('Even')

for i, r in enumerate(results):
    print('#%d %s' %(i+1, r))

# 연산처리를 줄이기 위해 마지막 숫자만 빼내서 연산처리.
# 1000개의 테스트 기준 으로 199ms 속도 나온다.(1회 측정)
# 마지막 숫자만 빼지 않고 숫자 그대로 사용 했을 경우. 206ms. 거의 비슷하다..

"""
results = []
for T in range(int(input())):
    number = int(input())
    if number % 2 == 1:
        results.append('Odd')
    else:
        results.append('Even')

for i, r in enumerate(results):
    print('#%d %s' %(i+1, r))

"""
