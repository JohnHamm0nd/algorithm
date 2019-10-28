"""
빼빼로 데이에 빼빼로를 들고 소개팅에서 바람을 맞은 태혁이를 지켜본 친구들은 그 비참함을 극대화하기 위해 태혁이가 바람을 맞으며 기다린 시간을 계산하기로 하였다.
소개팅 약속 시간은 정확히 2011년 11월 11일 오전 11시 11분이었으며 태혁이가 깨달음을 얻은 시간은 D일 H시 M분이었다.
깨달음을 주기 위해 바람이 얼마나 오랫동안 노력하였는지 계산하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 테스트 케이스의 수 T (T ≤ 10)가 주어진다.
테스트 케이스의 각 줄에는 3개의 정수 D (11 ≤ D ≤ 14), H (0 ≤ H ≤ 23), M (0 ≤ M ≤ 59) 이 주어진다.

[출력]
각각의 케이스마다 각 줄에 태혁이가 얼마나 오랫동안 바람을 맞았는지 분 단위로 출력한다.
만약 태혁이가 소개팅 약속 시간 전에 차였다면 놀리기엔 너무 불쌍하므로 -1을 출력한다.
"""

import sys

sys.stdin = open('4299.txt', 'r', encoding = 'UTF-8')

d_day = [11, 11, 11]

for T in range(int(input())):
    day = list(map(int, input().split()))
    times = []
    for d in range(3):
        times.append(day[d] - d_day[d])
    mins = times[0]*24*60 + times[1]*60 + times[2]
    if mins >= 0:
        print('#%d %d' %(T+1, mins))
    else:
        print('#%d %d' %(T+1, -1))
