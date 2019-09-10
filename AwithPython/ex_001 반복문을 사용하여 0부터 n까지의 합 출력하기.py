"""
반복문을 사용하여 0부터 n까지의 합 출력하기
"""

def  sum_number(number):
    sum = 0
    for n in range(number + 1): 
        sum += n
    return(sum)
    
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    print(sum_number(number))
