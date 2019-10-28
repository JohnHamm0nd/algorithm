"""
회문(palindrome) 확인하기
"""

def palindrome_check(string):
    n = 0
    while n <= len(string) - n:
        if string[n] != string[len(string) - n - 1]:
            return "회문이 아닙니다."
        n += 1
    return "회문입니다."


if __name__ == "__main__":
    string = input("회문(palindrome)을 확인할 문자 입력 :")
    print("%s 은(는) %s "%(string , palindrome_check(string)))
    
