"""
3개의 숫자를 입력으로 받고 3개의 숫자 중에 중간값을 가지는 숫자를 출력하세요. ex1) 2, 5, 3 => 3 ex2) 4, 6, 4 => 4
"""

numbers  = list(map(int, input('중간값을 구할 세 수를 입력하세요(스페이스바로 구분): ').split()))
numbers.sort()
print(numbers[1])
