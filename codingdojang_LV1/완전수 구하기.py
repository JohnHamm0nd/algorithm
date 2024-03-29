"""
자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다. 예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 // 1,2,4,7,14는 각각 28의 약수
입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하라.
"""

N = int(input("입력값 까지의 완전수 찾기: "))

for n in range(6, N+1):
    half = n // 2
    divisors = []
    for i in range(1, half+1):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        print(' %d 은 완전수 입니다.' %n)



# 짧은 코딩(연산량은 많을듯-약수를 숫자의 반까지만 구하면 되는데, 코드에서 제한시키지 않으므로)
num= int(input("숫자를 입력하시오 : "))
print([x for x in range(1, num+1) if x==sum(y for y in range(1, x) if x%y==0)])
