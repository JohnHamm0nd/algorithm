"""
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

1. 김씨와 이씨는 각각 몇 명 인가요?
2. "이재영"이란 이름이 몇 번 반복되나요?
3. 중복을 제거한 이름을 출력하세요.
4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
"""

names = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
name_list = names.split(',')

# 1
count_kim = 0
count_lee = 0

for name in name_list:
    if name[0] == '김':
        count_kim += 1
    elif name[0] == '이':
        count_lee += 1

print('#%s 김: %d    이: %d' %('1. ', count_kim, count_lee))
print()

# 2
print('#%s %d'%('2. ',name_list.count('이재영')))
print()

# 3
print('#%s %s'  %('3. ',' '.join(set(name_list))))
print()

# 4
print('#%s %s'  %('4. ',' '.join(sorted(list(set(name_list))))))
print()
