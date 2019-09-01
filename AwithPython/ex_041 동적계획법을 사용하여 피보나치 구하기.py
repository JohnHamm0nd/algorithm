"""
동적계획법을 사용하여 피보나치 구하기
"""

def fib(n):
    table[0] = 0
    table[1] = 1
    for i in range(n + 1):
        if i == 0 or i == 1:
            print("피보나치 %2d = %10d"%(i,table[i]))
        else:
            table[i] = table[i-1] + table[i-2]
            print("피보나치 %2d = %10d"%(i,table[i]))

if __name__ == "__main__":
    number = int(input("구하려는 피보나치 수열의 수를 입력하세요. : "))
    table = [0 for i in range(number+ 1)]
    fib(number)
    
"""
이미 39번 문제 푼 방법이 동적계획법인듯?
"""
