"""
파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.

Example:
codingDojang --> coding_dojang
numGoat30 --> num_goat_3_0

위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!

출처: UT past test
"""

string = input('Pothole_case 로 변환할 변수 입력: ')
new_string = ''

for s in string:
    if s.isdigit() or s.isupper():
        new_string += '_' + s.lower()
    else:
        new_string += s
print(new_string)


"""
# 다른풀이 1
# 정규식 사용
import re

pc = lambda src: re.sub("([A-Z0-9])", lambda m:"_"+m.group().lower(), src)

print(pc("codingDojang"))  # coding_dojang
print(pc("numGoat30"))     # num_goat_3_0

# 다른풀이 2
# 내가 푼것과 같은 방법. if elif 케이스를 나누지 않아도 된다. lower() 함수에 숫자 넣어도 작동 된다.
def to_pathole(s):
    res=''
    for c in s:
        if c.isupper():c='_'+c.lower()
        elif c.isdigit():c='_'+c
        res += c
    return res

print to_pathole('codingDojang')
print to_pathole('numGoat30')
"""
