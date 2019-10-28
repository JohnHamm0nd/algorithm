"""
문자와 숫자가섞인 문자열을 입력받을때 구별하여출력해라
input:
"c910m6ia 1ho"

output:
str : cma ho
int : 91061
"""

string = input('입력: ')

strr = ''
intt = ''
for s in string:
    if s.isdigit():
        intt += s
    else:
        strr += s

print('str: ', strr)
print('int: ', intt)


"""
# 다른방법 ( try-except 사용 )
str_input,int_input="",""
#ex:pa2th0n
for i in input():
    try:
        int(i)
        int_input+=i
    except:
        str_input+=i
print("str : ",str_input)
print("int : ",int_input)

# 짧은코딩
inp = input()
print('str : ',''.join(x for x in inp if not x.isdigit()),'\nint : ',''.join(x for x in inp if x.isdigit()))
"""
