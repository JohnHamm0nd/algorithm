"""
덧셈을 배운지 얼마 안 된 준환이는 덧셈에 아직도 어려움을 느낀다.
그래서 준환이는 N자리인 두 양수를 더하는 연습을 하기로 했다.
당신은 준환이를 위해 답안지를 만들어 주기로 했다.
두 양수가 주어질 때 두 수를 더한 결과를 구하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 첫 번째 줄에 두 양의 정수 A, B(1 ≤ A, B< 10100)가 공백으로 구분되어 주어진다.
두 수는 0으로 시작되지 않는다.

[출력]
각 테스트 케이스마다 A+B값을 출력한다. 첫 번째 자리가 0으로 시작해서는 안 된다. 
"""

import sys

sys.stdin = open('3260.txt', 'r', encoding = 'UTF-8')

for T in range(int(input())):
    print('#%d %d' %(T+1, sum(list(map(int, input().split())))))
    
"""
for T in range(int(input())):
    A, B = list(map(int, input().split()))
    print('#%d %d' %(T+1, A+B))
"""
