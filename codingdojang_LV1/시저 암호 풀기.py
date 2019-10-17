"""
시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데, 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는(여기서는 예를 들 때 3으로 지정하였다)알파벳이 출력되는 것이다.
예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.
"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input('암호화할 문자를 대문자로 입력: ')
n = int(input('암호키(숫자) 입력: '))
new_word = ''

for w in word:
    n = n % 26
    if alphabet.index(w) + n < 26:
        new_word = new_word + alphabet[alphabet.index(w) + n]
    else:
        new_word = new_word + alphabet[alphabet.index(w) + n - 26]
print(new_word)
