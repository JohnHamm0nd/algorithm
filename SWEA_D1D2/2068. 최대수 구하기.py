"""
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
출력
#1 99
#2 123
#3 76
"""

import sys

sys.stdin = open('2068.txt', 'r', encoding = 'UTF-8')


T = int(input())
numbers = []
for t in range(T):
    numbers.append(max(list(map(int, input().split()))))

for idx, d in enumerate(numbers):
    print("#{} {}".format(idx+1, d))


"""
다른 답.
n = int(input())

nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

for idx, num in enumerate(nums):
    print('#{} {}'.format(idx+1, max(num)))
"""
"""
2070문제와 마찬가지로 연산을 어디서 하는게 좋을지 생각.
"""
