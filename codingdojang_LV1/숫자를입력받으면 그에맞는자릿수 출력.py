"""
(난이도:기초) 숫자를 입력받으면 그에해당하는 자릿수를 출력하는 코드를 작성하라.
입력 : 156 출력 : 100의자리수
입력 : 18961 출력 : 10000의자릿수
"""

number = input('숫자 입력: ')
print('1%s의 자릿수' %('0'*(len(number)-1)))

"""
# 방법 2
print("{}의 자리수".format(10**(len(input())-1)))
"""
