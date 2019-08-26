"""
점수 분포 출력하기
"""

a = [ 75, 25, 6, 73, 43, 46, 31, 13, 60, 90, 5, 43, 35, 65, 100, 28, 83, 95, 35, 45 ]
history = [0] * 11

for i in a:
    history[i // 10] += 1

for i in range(len(history)):
    print("{0} 점대 - : {1} 명".format(i*10,history[i]))
