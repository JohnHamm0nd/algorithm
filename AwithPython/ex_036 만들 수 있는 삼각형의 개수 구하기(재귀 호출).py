"""
만들 수 있는 삼각형의 개수 구하기(재귀 호출)
"""

cnt = 0
def count_triangle(n):
    global cnt
    for a in range(1, n -1):
        for b in range(1, n - a):
            c = n - a - b
            if a <= b and b <= c and a + b > c:
               cnt += 1
               print(a, b, c)
    return cnt


if __name__ == "__main__":
    number = int(input("삼각형의 총 길이를 입력하세요. : "))
    print("만들 수 있는 삼각형의 갯수 : %d"%(count_triangle(number)))                

