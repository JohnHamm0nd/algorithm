"""
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자.
입력 - 화면에서 숫자로 된 문자열을 입력받는다.
"4546793"
출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
"454*67-9-3"
"""

input_string = "4546793"
new_string = ''
for i in range(len(input_string)-1):
    if int(input_string[i]) % 2 == 0 and int(input_string[i+1]) % 2 == 0:
        new_string = new_string + input_string[i] + "*"
    elif int(input_string[i]) % 2 == 1 and int(input_string[i+1]) % 2 == 1:
        new_string = new_string + input_string[i] +"-"
    else:
        new_string = new_string + input_string[i]
new_string = new_string + input_string[-1]
print(new_string)


# 정규식을 이용하는 방법
import re
print(re.sub(r'(([02468]{2,})|([13579]{2,}))', lambda x:'*'.join(x.group(2)) if x.group(2) else '-'.join(x.group(3)), input(":")))
