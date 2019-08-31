"""
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 1이상 10000이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

import sys

sys.stdin = open('2029.txt', 'r', encoding = 'UTF-8')


result = []
for T in range(int(input())):

    a, b = list(map(int, input().split()))
    mok = a // b
    namuji = a % b
    result.append(str(mok)+" "+str(namuji))

for idx, r in enumerate(result):
    print("#{} {}".format(idx+1, r))


"""
다른답안
n = int(input())

for i in range(n):
    x = input().split()
    a, b = int(x[0]), int(x[-1])
    print(f'#{i+1} {a//b} {a%b}')
"""
