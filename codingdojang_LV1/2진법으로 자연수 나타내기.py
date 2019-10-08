"""
2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다. 예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 1001001으로 표현한다. 
어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.
"""

number = int(input('2진법으로 나타낼 자연수를 입력하세요: '))
c_list = []

while number > 1:
    c_list.insert(0, number % 2)
    number = number // 2
c_list.insert(0, number)

print(''.join(map(str, c_list)))
