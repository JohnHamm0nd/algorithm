"""
배열 [a, b, c, d]를 입력하면 배열[bcd, acd, abd, abc]를 출력하는 코드를 작성하시오.
(단, 나눗셈 사용 금지)
입출력되는 배열은 어떤 형식이든 상관없습니다.

입력 예시
2, 6, 4, 7

출력 예시
168, 56, 84, 48
"""

def brr(a, b, c, d):
    x1 = b*c*d
    x2 = a*c*d
    x3 = a*b*d
    x4 = a*b*c
    return x1, x2, x3, x4

arr = [2, 6, 4, 7]

print(brr(arr[0], arr[1], arr[2], arr[3]))
