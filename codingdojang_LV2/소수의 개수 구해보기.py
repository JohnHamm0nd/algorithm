"""
2이상 1000이하 자연수의 집합에서 소수의 개수를 구하는 알고리즘을 작성하시오.
"""

numbers = []
for i in range(2, 1001):
    numbers.append(i)
for i in range(2, 501):
    j = 2
    while i * j < 1001:
        if i * j in numbers:
            numbers.remove(i*j)
        j += 1
print(len(numbers))
