"""
Write a program that lets the user enter in an odd positive integer (you may assume the input is always valid), and prints out an ASCII art letter N made using the character N.

If the input is 1, the output is:
N

If the input is 3, the output is:
N N
NNN
N N

If the input is 5, the output is:
N   N
NN  N
N N N
N  NN
N   N

If the input is 7, the output is:
N     N
NN    N
N N   N
N  N  N
N   N N
N    NN
N     N

The pattern continues on like this. The output may contain trailing spaces.
"""

N = int(input('입력: '))

for i in range(N-1):
    if i == 0:
        print('N', end=''), print(' '*(N-2-i), end=''), print('N')
    if i == N-2:
        print('N', end=''), print(' '*(i), end=''), print('N')
    else:
        print('N', end=''), print(' '*i, end=''), print('N', end=''), print(' '*(N-2-i), end=''), print('N')
