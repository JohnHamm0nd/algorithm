"""
배열을 사용하여 16진수 변환하기
"""

d = "0123456789ABCDEFGHIJ"

def f(n):
    if n > 0:
        f(n // 16)
        print("%c"%d[n % 16], end="")


if __name__ == "__main__":
    n = int(input("16진수로 변환할 10진수 입력 :"))
    f(n)
