"""
배열채우기(2)
"""
def calc_array(number):
    a[0] = 1
    i = 2
    while i < number:
        a[i] = a[i // 2] + 1
        i = i + 1
    return a

if __name__ == "__main__":
    number = int(input("배열의 갯수를 입력하세요. : "))
    a = [1] * number
    print(calc_array(number))
