"""
초보자 프로그래머 홍길동은 사용자가 입력한 양의정수(범위는 int)각 자리수를 더해 출력하는 프로그램을 만들고 싶어한다. 
ex) 5923의 결과는 5+9+2+3인 19이다.
ex) 200의 결과는 2+0+0인 2이다.
ex) 6719283의 결과는 6+7+1+9+2+8+3인 36이다.
"""

numbers = list(map(int, input('각 자리의 합을 구할 수 입력: ')))
print(sum(numbers))


"""
# 다른방법 1 ( eval 함수 사용 ) 
print(eval('+'.join(input())))

# 다른방법 2 ( map 함수 사용 후 바로 더함 )
print(sum(map(int, input('양의 정수: '))))

# 다른방법 3 ( for문 사용하여 더함 )
num = input("숫자를 넣어주세요: ")
print(sum(int(n) for n in num))
"""
