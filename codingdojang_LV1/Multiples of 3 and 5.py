"""
[문제]
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

[번역]
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
"""

multiples_sum = 0

"""
for i in range(1000):
    if i % 3 == 0:
        multiples_sum += i
    elif i % 5 == 0:
        multiples_sum += i
print(multiples_sum)
# if elif 사용
"""

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples_sum += i
print(multiples_sum)
# if or 사용


# print(sum([x for x in range(1000) if x%3==0 or x%5==0]))
# 다른답안(List Comprehension)
