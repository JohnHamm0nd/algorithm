"""
홀수와 짝수의 개수를 구하는 프로그램을 만들어라.
[3, 4, 5, 6, 7]
= 홀수 3개, 짝수 2개
[12, 16, 22, 24, 29]
= 홀수 1개, 짝수 4개 
[41, 43, 45, 47, 49]
= 홀수 5개, 짝수 0개
홀수 : 2로 나누어 떨어지지 않는 정수
짝수 : 2로 나누어 떨어지는 정수
"""

list_a = [3, 4, 5, 6, 7]
list_b = [12, 16, 22, 24, 29]
list_c = [41, 43, 45, 47, 49]

def eo_check(n_list):
     even = 0
     odd = 0
     for n in n_list:
         if n % 2 == 0:
             even += 1
         else:
             odd += 1
     return even, odd
    
print('짝수: %d개 , 홀수: %d개' %(eo_check(list_a)))
print('짝수: %d개 , 홀수: %d개' %(eo_check(list_b)))
print('짝수: %d개 , 홀수: %d개' %(eo_check(list_c)))
