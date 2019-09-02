"""
2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
3
3 8
7 7
369 123
출력
#1 <
#2 =
#3 >
"""

import sys

sys.stdin = open('2070.txt', 'r', encoding = 'UTF-8')

T = int(input())
data = []
for t in range(T):
    a, b = (list(map(int, input().split())))
    if a > b:
        data.append(">")
    elif a == b:
        data.append("=")
    else:
        data.append("<")

for idx, d in enumerate(data):
    print("#{} {}".format(idx+1, d))


"""
다른 답.
n = int(input())

nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

for idx, num in enumerate(nums):
    if num[0] < num[-1]:
        res = '<'
    elif num[0] == num[-1]:
        res = '='
    else:
        res = '>'
    print('#{} {}'.format(idx+1, res))
"""
"""
다른 답(a)과 내답과 차이(b)
a 에서는 입력을 받아 저장 시킨 후 출력 할 때 비교연산을 하여 출력하였다. 이 경우 입력받을 때 연산은 없지만 출력 할 때 연산이 몰린다. 연산을 모아두었다가 한꺼번에 연산을 하는 방법.
b 에서는 입력 받을 때 마다 연산을 하여 처리한 결과를 저장해 두었다가 뒤에서 출력만 하는 방법이다. 입력 받을 때마다 연산을 하지만 뒤에서 한꺼번에 연산을 할 필요는 없다. 분할연산 방법. 앞에서 연산을 하여 결과값만 저장하므로 입력받은 값은 없어진다.
a는 연산량이 너무 많을 때 문제가 발생 할 가능성이 있다 - 다중작업이 발생할 경우 연산할 자원이 부족할수 있다.
b는 잦은 I/O? cpu와 주고받는작업이 많아져 비효율이 발생할 수 있다. - 한번에 왔다갔다 할 것을 여러번 왔다갔다 함.
"""
