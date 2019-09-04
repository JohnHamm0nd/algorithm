"""
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
"""

import sys

sys.stdin = open('1209.txt', 'r')

for T in range(10):
    N = int(input())
    arr =  []
    num3 = 0
    num4 = 0
    for T in range(100):
        arr.append(list(map(int, input().split())))
        max_num = 0
    for i in range(len(arr)):
        num1 = 0
        num2 = 0
        for j in range(len(arr)):
            num1 += arr[i][j]
            num2 += arr[j][i]
            if i == j:
                num3 += arr[i][j]
                num4 += arr[i][len(arr) - 1- j]
        if num1 > max_num:
            max_num = num1
        if num2 > max_num:
            max_num = num2
        if num3 > max_num:
            max_num = max3
        if num4 > max_num:
            max_num = num4

    print('#%d %d' %(N, max_num))
            

"""
        while i <= len(arr):
            num1 = 0
            num2 = 0
            while j  <= len(arr):
                num1 += arr[i][j]
                num2 += arr[j][i]
                if num1 > max_num:
                    max_num = num1
                if num2 > max_num:
                        max_num = num2
    print(max_num)
"""
