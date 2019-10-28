"""
반복문을 사용하여 조합(nCr) 구하기
"""

def combination(n, r):
    A = 1
    B = 1
    while r >= 1:
        A *= n-r+1
        B *= r
        r -= 1
    C = A // B
    return C

""" 
    for i in range(n-r+1, n+1):
        print(i)
"""

if __name__ == "__main__":
    n, r =  list(map(int, input("경우의 수를 구할 두 수을 입력하세요 : ").split()))
    print("{}개중 {}개를 선택할수 있는 조합의 갯수는 : {} 개".format(n, r, combination(n,r)))
