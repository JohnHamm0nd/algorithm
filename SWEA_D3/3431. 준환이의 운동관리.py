"""
최근 경도비만 판정을 받은 준환이는 적절한 몸을 유지하기 위하여 1주일에 L분 이상 U분 이하의 운동을 하여야 한다.
준환이는 이번 주에 X분만큼 운동을 하였다.
당신은 준환이가 제한되어 있는 시간을 넘은 운동을 한 것인지, 그것이 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력하는 프로그램을 작성해야 한다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 세 정수 L, U, X(0≤ L ≤ U ≤ 107, 0 ≤ X ≤ 107)가 공백으로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 I가 필요한 양보다 더 많은 운동을 하고 있다면 -1을 출력하고, 아니라면 추가로 몇 분을 더 운동해야 하는지 출력한다. 
"""

import sys

sys.stdin = open('3431.txt', 'r', encoding = 'UTF-8')


def check_time(L, U, X):
    if X < L:
        return L-X
    elif L < X < U:
        return 0
    else:
        return -1


for T in range(int(input())):
    L, U, X = list(map(int, input().split()))
    print('#%d %d' %(T+1, check_time(L, U, X)))
