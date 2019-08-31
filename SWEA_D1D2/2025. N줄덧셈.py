"""
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
단, 주어질 숫자는 10000을 넘지 않는다.

[예제]
주어진 숫자가 10 일 경우 출력해야 할 정답은,
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
"""

import sys

sys.stdin = open('2025.txt', 'r', encoding = 'UTF-8')

number = int(input())

sum = 0
for n in range(1, number + 1):
    sum += n
print(sum)


"""
다른답안
n = int(input())
print(sum([i for i in range(1, n+1)]))
"""
