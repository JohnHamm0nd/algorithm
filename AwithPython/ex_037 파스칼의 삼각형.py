"""
파스칼의 삼각형
"""

def combination(n, r):
    if r == 0:
        return 1
    return (n-r+1) * combination(n, r-1)  // r

if __name__ == "__main__":
    number = int(input("파스칼의 삼각형을 구할 수를 입력해 주세요: "))
    for i in range(number):
        for j in range(i + 1):
            print(combination(i, j), end = "    ")
        print()


"""
위에서부터 내려오면서 양쪽으로 1을 더하는 방법도 있다.
 nCr 방법으로 풀면 간단하기 때문에 그렇게 하였다
"""
