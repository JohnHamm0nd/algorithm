"""
문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
"""

string = input('문자열 입력: ')
new_string = ''
new_string += string[0]
count = 1
for s in string[1:]:
    if s != new_string[-1]:
        new_string += str(count)
        new_string += s
        count = 1
    else:
        count += 1
new_string += str(count)
print(new_string)


"""
# 다른 답안(방법은 거의 같다)
s = 'aabcccaaaaas'

result = s[0]  # 첫번째 값을 결과에 넣는다
count  = 0   #

for st in s:
    if st == result[-1]:  #
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)
"""
