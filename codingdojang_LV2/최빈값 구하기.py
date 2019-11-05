"""
리스트에 있는 숫자들의 최빈값을 구하는 프로그램을 만들어라.

[12, 17, 19, 17, 23] = 17
[26, 37, 26, 37, 91] = 26, 37
[28, 30, 32, 34, 144] = 없다

최빈값 : 자료의 값 중에서 가장 많이 나타난 값 
① 자료의 값이 모두 같거나 모두 다르면 최빈값은 없다.
② 자료의 값이 모두 다를 때, 도수가 가장 큰 값이 1개 이상 있으면 그 값은 모두 최빈값이다.
"""

n_list = [[12, 17, 19, 17, 23],
         [26, 37, 26, 37, 91],
         [28, 30, 32, 34, 144],
         [10, 10, 10, 10, 10]]
         
for numbers in n_list:
    n_dict = {}
    for n in numbers:
        if n in n_dict:
            n_dict[n] += 1
        else:
            n_dict[n] = 1
    mode = []
    if len(n_dict) == 1 or len(n_dict) == len(numbers):
        print(numbers, '= 없다')
    else:
        mode_count = max(n_dict.values())
        for e in n_dict.keys():
            if n_dict[e] == mode_count:
                mode.append(e)
        print(numbers, '=', mode)
