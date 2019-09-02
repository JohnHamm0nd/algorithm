# -*- coding: utf-8 -*- 
"""
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
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
#1 200
#2 208
#3 121
"""

"""
#예외처리

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

# 입력받은 값 중 홀수 값을 더하여 반환.
def numplus(numbers):
    numsum = 0
    for i in numbers:
        if i % 2 != 0:
            numsum += i
    return numsum


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
                numsum.append(numplus(numbers))
                flag2 += 1
            else:
                print("숫자를 10개 입력해 주세요. 각 수는 0이상 10000 이하의 정수입니다.")
    else:
        print("잘못입력 하셨습니다, 숫자를 입력해 주세요.")
        continue
    flag1 = False

for i, num in enumerate(numsum):
    print("#{i}, {num}".format(i=i+1, num=num))
    

"""

import sys

sys.stdin = open('2072.txt', 'r', encoding = 'UTF-8')

T = int(input())

for t in range(T):
    num_sum = 0
    num_list = list(map(int, input().split()))
    for num in num_list:
        if num % 2 != 0:
            num_sum += num
    print("#{} {}".format(t+1, num_sum))

