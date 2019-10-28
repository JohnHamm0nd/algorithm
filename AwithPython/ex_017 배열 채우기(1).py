"""
배열 채우기(1)
"""


def calc_array(number):
    a[0] = 1
    a[1] = 1
    i = 2
    while i <= number - 1:
        a[i] = a[i-1] + a[i -2] + 1
        i = i + 1
    return a

if __name__ == "__main__":
    number = int(input("배열의 갯수를 입력하세요. : "))
    a = [1] * number
    print(calc_array(number))
