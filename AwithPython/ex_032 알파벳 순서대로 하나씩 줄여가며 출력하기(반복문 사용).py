"""
알파벳 순서대로 하나씩 줄여가며 출력하기(반복문 사용)
"""

n = 0
while n <= ord("Z") - ord("A"):
    for a in range(ord("A"), ord("Z") + 1 - n): 
        print(chr(a), end = " ")
    print()
    n += 1
