"""
방송사에서 생방송 자막 송출을 담당하고 있는 재경이는 한글 타자가 무려 1000에 육박한다.
누구보다 빠른 한글 타자를 보유하고 있지만 치명적인 단점이 있다. 영어 타자의 오타가 극심하게 발생한다.
재경이는 어떤 단어를 쓸 때에 오타를 특정한 방법으로 발생시킨다.
치고자 하는 단어와 길이는 동일한 단어를 쓰지만, i번째 문자에다가 원래 단어의 (i-1) 번째, i 번째, (i+1) 번째 문자 중 무엇이든 쳐버린다.
특히 제일 첫 문자는 첫 문자와 그 다음 문자 중 하나를 쓸 수 있고, 마지막 문자는 마지막과 그 앞의 문자를 쓸 수 있다.
예를 들어서, apa 라는 단어에서 재경이가 낼 수 있는 오타는 aaa, aap, apa, app, paa, pap, ppa, ppp 중 하나를 칠 수 있는 것이다.
단어가 주어졌을 때에 재경이가 칠 수 있는 서로 다른 단어의 개수를 구하여라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 재경이가 원래 치고자 하는 단어가 주어진다. 단어의 길이는 1,000 이하의 자연수이다. 단어는 모두 소문자 알파벳으로 구성되어 있다.

[출력]
각 테스트 케이스마다 재경이가 칠 수 있는 단어의 종류를 10억7(=10^9+7) 로 나눈 나머지를 출력하라.
"""

import sys

sys.stdin = open('7853.txt', 'r', encoding = 'UTF-8')


for T in range(int(input())):
    word = input()
    cases = []
    noc = 1
    for i in range(len(word)):
        if i == 0:
            if word[i] == word[i+1]:
                cases.append(1)
            else:
                cases.append(2)
        elif i == len(word)-1:
            if word[i] == word[i-1]:
                cases.append(1)
            else:
                cases.append(2)
        else:
            if word[i-1] == word[i] and word[i] == word[i+1]:
                cases.append(1)
            elif word[i-1] != word[i] and word[i] != word[i+1] and word[i-1] != word[i+1]:
                cases.append(3)
            else:
                cases.append(2)
    for c in cases:
        noc *= c
    print('#%d %d' %(T+1, noc))

# 파이썬이 없어서 채점 불가.
# 중복되는 오타의 종류는 없나?
