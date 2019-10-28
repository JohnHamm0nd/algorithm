"""
최적화한 조합
"""

def combination(n, r):
    if r == 0:
        return 1
    return (n-r+1) * combination(n, r-1)  // r

if __name__ == "__main__":
    n, r =  list(map(int, input("경우의 수를 구할 두 수을 입력하세요 : ").split()))
    print("{}개중 {}개를 선택할수 있는 조합의 갯수는 : {} 개".format(n, r, combination(n,r)))

"""
20번 문제에서 이미 최적화함(재귀함수 1번만 사용)
"""
