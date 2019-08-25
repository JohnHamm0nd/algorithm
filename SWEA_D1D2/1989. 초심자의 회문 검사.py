"""
"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

[제약 사항]
각 단어의 길이는 3 이상 10 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

import sys
sys.stdin = open('1989.txt', 'r')


T = int(input())
for t in range(T):
    string = input()
    palin = string[:(len(string) // 2)]
    palin = palin[::-1]
    if palin == string[-(len(string) // 2):]:
        result = 1
    else:
        result = 0
    print(f'#{t + 1} {result}')
# 입력받은 문자를 반으로 쪼개어 앞부분을 뒤집어 뒷부분과 비교, 밑에 있는 방법이 더 효율적인듯 문자열 길이가 엄청나게 길어지면 이게 더 효율적 일 수도..

"""
다른답안: 입력 받은 문자를 모두 뒤집어 입력받은 문자와 같은지 비교.
T = int(input())
for _ in range(T):
    s = input().strip()
    print(s)
    if s == s[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{_+1} {result}')
"""
