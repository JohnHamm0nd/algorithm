"""
모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6
출처:http://regex101.com/quiz/
"""

string = input('입력: ')
new_string = ''
switch = 0
for i in range(len(string)):
    if switch == 1:
        switch = 0
        if string[i].isdigit():
            new_string += '*'
        else:
            new_string += string[i]
    else:
        new_string += string[i]
        switch = 1
print(new_string)
