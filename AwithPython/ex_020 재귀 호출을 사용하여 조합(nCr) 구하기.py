"""
재귀 호출을 사용하여 조합(nCr) 구하기
"""

def combination(n, r):
    if r == 0:
        return 1
    return (n-r+1) * combination(n, r-1)  // r

if __name__ == "__main__":
    n, r =  list(map(int, input("경우의 수를 구할 두 수을 입력하세요 : ").split()))
    print("{}개중 {}개를 선택할수 있는 조합의 갯수는 : {} 개".format(n, r, combination(n,r)))
