"""
당신은 실력있는 A국의 스파이다.
어느 날 당신은 옆 나라 B국이 첨단 무기를 만들려 한다는 사실을 알게 되었고
당국은 당신에게 그 문서를 훔쳐오라고 말했다.
막상 거기에 도착해보니 경비가 매우 삼엄해 당신은 도움이 필요했다.
그러나 주위에 있는건 노트북 뿐,
메일로 통신을 하게 되면 인터넷을 감시하고 있는 B국이 그 사실을 알게 된다.
일반 시저 암호도 들키게 될 위험이 크므로 당신은 피보나치 시저 암호를 고안해 만들기로 했다.
문제- 피보나치 시저 암호를 만드시오
맨 처음 줄에는 정수인 암호키가 주어진다. (0 < N < 10000 )
그 다음 줄에는 변환하고 싶은 문자열이 주어진다.
문자열의 길이만큼 피보나치 수로 바꿔 문자열을 바꾸시오.
(예를 들어 암호키가 4 라면 수열은 1,4,5,9 . . . 로 되어 그 숫자만큼 문자열을 돌린다.)
입력에 소문자는 들어가 있지않으며 기호나 숫자가 들어가 있을 시 그대로 둔다. ( 공백 포함)
(시작은 무조건 1이다.)

입력)
1
AAAAA
1
HELLO, WORLD!
3
ABCDE

출력)
BBCDF
IFNOT, EMBTG!
BEGKP
"""

al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 1
b = int(input('암호키입력：'))
c = a + b
word = input('암호입력: ')
password = ''

if word[0] in al:
    password += al[al.index(word[0])+a]
else:
    password += word[0]
if word[1] in al:
    password += al[al.index(word[1])+b]
else:
    password += word[1]
for w in range(2, len(word)):
    if word[w] in al:
        if al.index(word[w])+c >= 26:
            password += al[(al.index(word[w])+c) % 26]
        else:
            password += al[al.index(word[w])+c]
        a = b
        b = c
        c = a + b
    else:
        password += word[w]
print(password)


"""
#다른코드
＃아스키코드를　이용한　간단한　방법
def code(n, string):
  s, ret = 1, ''
  for i in string:
    if i.isupper(): 
      ret += chr((ord(i)-65+s)%26+65)
      s, n = n, s+n
    else: ret += i
  return ret
"""
