"""
준홍이에게는 카드 두 세트가 있다.
각 카드 세트는 1번 카드부터 N번 카드, 1번 카드부터 M번 카드로 구성되어 있다.
심심했던 준홍이는 각 카드 세트에서 카드 한 장씩을 골랐다.
그리고 각 카드에 적힌 숫자를 더해보았다.
1번 카드와 1번 카드를 골랐다면 카드에 적힌 숫자의 합은 2가 될 것이고, N번 카드와 M번 카드를 골랐다면 카드에 적힌 숫자의 합은 N+M이 될 것이다.
문득 준홍이는 각 카드 세트에서 카드를 한 장씩 골라서 카드에 적힌 숫자를 합한 결과 중, 등장할 확률이 가장 높은 숫자는 어떤 숫자일지 궁금해졌다.
단, 카드 세트에서 어떤 카드를 선택할 확률은 모두 동일하다고 가정한다.
이를 계산하는 프로그램을 작성하라.
 
[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 개의 x정수 N, M(4 ≤ N, M ≤ 20)이 공백 하나로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
선택한 두 카드에 적힌 숫자의 합 중 등장할 확률이 가장 높은 것들을 오름차순으로 공백을 사이에 두고 한 줄에 모두 출력한다.
"""

import sys

sys.stdin = open('7102.txt', 'r', encoding = 'UTF-8')


for T in range(int(input())):
    N, M = map(int, input().split())
    sum_num = []
    count_list = []
    max_count_list = []
    for n in range(1, N+1):
        for m in range(1, M+1):
            sum_num.append(n+m)
    print(sorted(sum_num))
    for c in range(2, N+M+1):
        count_list.append(sum_num.count(c))
    max_count = max(count_list)
    print(count_list)
    for m in range(len(count_list)):
        if count_list[m] == max_count:
            max_count_list.append(m+2)
    print(max_count_list)
