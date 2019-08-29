"""
주어진 숫자부터 0까지 순서대로 찍어보세요
n, n-1, n-2, ... , 0
"""
import sys

sys.stdin = open('1545.txt', 'r', encoding = 'UTF-8')


N = int(input())

for i in range(N+1):
    print(N-i, end = ' ')

"""
다른답안
n = int(input())
for i in range(n, -1, -1):
    print(i, end=' ')
"""
