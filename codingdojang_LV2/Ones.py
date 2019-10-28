"""
출처: programming challenges

2나 5로 나눌 수 없는 0 이상 10,000 이하의 정수 n이 주어졌는데, n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다. 그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?

Sample Input
3
7
9901

Sample Output
3
6
12
"""
# 0입력하면 종료.
# 풀이1. 입력 된 수를 계속 더하여 모든 자리 숫자가 1이 나올 때 까지 구한다. -> 너무 많은 연산
# 풀이2. 모든 자리 숫자가 1이라고 하였으므로 1, 11, 111, 1111, 11111... 순으로 1를 계속 붙인 후 입력된 수로 나누어 떨어질때까지 구한다.

ones = 1
ones_plus = 1
while 1:
    number = int(input())
    if number == 0:
        break
    else:
        while ones % number != 0:
            ones += 10**ones_plus
            ones_plus += 1
        #print(len(str(ones))) # ones 의 길이로 구하는방법.
        print(ones_plus) # one_plus 와 길이가 같음.
