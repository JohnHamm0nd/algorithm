"""
A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
버전은 다음처럼 "." 으로 구분된 문자열이다.
버전 예) 1.0.0, 1.0.23, 1.1
두 개의 버전을 비교하는 프로그램을 작성하시오.
다음은 버전 비교의 예이다.
0.0.2 > 0.0.1
1.0.10 > 1.0.3
1.2.0 > 1.1.99
1.1 > 1.0.1
1.0 > 1.0.1
"""


versions = [['0.0.2', '0.0.1'],
                    ['1.0.10', '1.0.3'],
                    ['1.2.0', '1.1.99'],
                    ['1.1', '1.0.1'],
                    ['1.0', '1.0.1'],
                    ['1.3.1', '1.3.1']]

# 라이브러리 사용하지 않는 방법.
for v in versions:
    v_a = v[0].replace('.', '')
    v_b = v[1].replace('.', '')
    max_length = max(len(v_a), len(v_b))
    v_a = v_a + '0'*(max_length-len(v_a))
    v_b = v_b + '0'*(max_length-len(v_b))
    
    for a, b in zip(v_a, v_b):
        if a > b:
            print(v[0], '>', v[1])
            break
        elif a < b:
            print(v[0], '<', v[1])
            break
    else:
        print(v[0], '=', v[1])



# zip_longest 라이브러리 사용시
from itertools import zip_longest

def compare(left, right):
    left_vars = map(int, left.split('.'))
    right_vars = map(int, right.split('.'))
    for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
        if a > b:
            return '>'
        elif a < b:
            return '<'
    return '='
    

for v in versions:
    print('{0[0]} {1} {0[1]}'.format(v, compare(*v)))
