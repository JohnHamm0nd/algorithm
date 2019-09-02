"""
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
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
#1 24
#2 29
#3 27
"""


"""
# 모든 케이스, 예외처리.

# 입력받은 테스트 횟수가 숫자가 맞는지 확인, 숫자이면 True 반환, 숫자가 아니면 False 반환.
def typecheck(numbers):
    try:
        int(numbers)
        return True
    except:
        return False

# 입력받은 숫자가 정수 값인지 확인, 정수 값이면 split 하여 리스트로 반환, 아니면 False 반환.
def numtypecheck(numbers):
    try:
        numbers = list(map(int, numbers.split()))
        return numbers
    except:
        return False

# 입력받은 숫자가 0이상 10000이하의 값인지 확인.
def numcheck(numbers):
    for i in numbers:
        if 0 <= i <= 10000:
            return True
        else:
            return False

# 입력받은 값의 평균 반환.
def numavg(numbers):
    numsum = 0
    for i in numbers:
        numsum += i
    return numsum / len(numbers)


flag1 = True
flag2 = 0
numsum = []

while flag1:
    nt = input("테스트 횟수 입력")
    if typecheck(nt):
        nt = int(nt)
        print("10개의 수를 입력해 주세요.(각 수는 0이상 10000 이하의 정수입니다)")
        while flag2 != nt:
            numbers = input("")
            numbers = numtypecheck(numbers)
            if numbers and len(numbers) == 10 and numcheck(numbers):
                numsum.append(numavg(numbers))
                flag2 += 1
            else:
                print("숫자를 10개 입력해 주세요. 각 수는 0이상 10000 이하의 정수입니다.")
    else:
        print("잘못입력 하셨습니다, 숫자를 입력해 주세요.")
        continue
    flag1 = False

for i, num in enumerate(numsum):
    print("#{i}, {num}".format(i=i+1, num=round(num)))

"""

import sys

sys.stdin = open('2071.txt', 'r', encoding = 'UTF-8')


T = int(input())

for t in range(T):
    num_list = list(map(int, input().split()))
    print("#{} {}".format(t+1, round(sum(num_list)/len(num_list))))
