"""
자연수 n이 있다. f(n)=(n의 양의 약수의 합)이라고고 하자. 자연수 n이 어떤 k에 대하여 등식 n = 1 + k(f(n)-n-1)을 만족했을 때, n을 k-초완전수라고 부른다.
n이 완전수라는 것은 n이 1-초완전수라는 것이라는 명제와 동치이다. 예를 들어, 21은 2-초완전수이고 301은 6-초완전수이다.
자연수 N을 입력받고 N 이하의 k-초완전수와 그때의 k를 순서쌍으로 출력하는 프로그램을 작성하라.

<예시> 1. 입력 1000 2. 출력 (6,1) (21,2) (28,1) (301,6) (325,3) (496,1) (697,12)
"""

number = int(input('입력: '))

for i in range(1, number+1):
    prime = []
    for j in range(1, (i//2)+1):
        if i % j == 0:
            prime.append(j)
    prime.append(i)
    cho = 1
    while 1 + cho * (sum(prime) - i - 1) <= i and (sum(prime) - i - 1) > 1:  # (sum(prime) - i - 1) >0 , (sum(prime) - i - 1) > 1
        if  1 + cho * (sum(prime) - i - 1) == i:
            print('(%d, %d)' %(i, cho))
        cho += 1
