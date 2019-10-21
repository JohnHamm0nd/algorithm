"""
소수 구하기(에라토스테네스의 체)
"""

TRUE = 1
FALSE = 0

def calc_prime(number):
    check = [TRUE] * number 
    check[0] = FALSE
    check[1] = FALSE
    i = 2
    while i < number:
        j = 2
        while i*j < number:
            check[i*j] = FALSE
            j = j + 1
        i = i + 1
    for i in range(0, len(check)):
        if check[i] == TRUE:
            print(i, end = ' ')
    print()
    print("소수의 갯수는: %d"%check.count(TRUE))
    
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    calc_prime(number)
    
"""
불완전 - 제거되지 않는 소수 있음. 
먼저 가장 작은 소수를 찾고 그 후 찾은 소수에 배수를 하여 제거해야 하는데
찾지 않고 2, 3, 5, 7, 9 의 배수만 제거하여 그렇다.
8, 9번 문제의 소수 찾기 방법에 배수를 하여 제거하는 방법을 사용하면 좋을듯.
연습문제 풀이의 경우 모두 소수라고 가정하고 그 후 2부터 3, 4, 5, 6 ~ n 까지 배수 하여 모두 제거.
-> 연습문제와 거의 같은 방법으로 풀었다.
"""
