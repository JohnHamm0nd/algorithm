"""
경표는 아래와 같이 삼각형 모양으로 숫자를 쌓기로 했다.
1층에는 1개, 2층에는 3개, 3층에는 5개, … 와 같이 쌓는다.

위와 같이 경표는 끝도 없이 피라미드를 쌓을 때, N층의 제일 왼쪽, 오른쪽에 쓰게 될 숫자가 무엇일지 예측해보자.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 층의 번호 N(1≤N≤10^9)이 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
각 테스트 케이스마다 N층의 제일 왼쪽, 오른쪽에 쓰게 될 숫자를 공백으로 구별하여 출력한다.
"""

import sys

sys.stdin = open('8016.txt', 'r', encoding = 'UTF-8')


def left(N):
    if N <= 1:
        return 1
    else:
        return left(N-1) + ((N*2-3)*2)
        
def right(N):
    if N <= 1:
        return 1
    else:
        return right(N-1) + ((N*2-1)*2)
        
for T in range(int(input())):
    N = int(input())
    print('#%d %d %d' %(T+1, left(N), right(N)))

# 파이썬 없어서 채점 불가
