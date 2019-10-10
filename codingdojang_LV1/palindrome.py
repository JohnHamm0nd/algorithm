"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다. 
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""

def palindrome_check(string):
    n = 0
    while n <= len(string) - n:
        if string[n] != string[len(string) - n - 1]:
            return 0
        n += 1
    return string
    
for i in range(999, 99, -1):
    check_p = str(i * i)
    n = 0
    if palindrome_check(check_p):
        print(check_p)
        break
    

"""
# 다른방법 
# s == s[::-1] <- 파이썬에서 펠린드룸 문자열을 확인 할 수 있는 간편한 방법이다.
def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

def main():
  m = 0
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      n = i * j
      if is_palindrome(n) and m < n:
        m = n
  print(m)
"""
