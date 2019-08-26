"""
등수 구하기
"""

a = [ 75, 25, 6, 73, 43, 46, 31, 13, 60, 90,5, 43, 35, 65, 100, 28, 83, 95, 35, 45]

rank = [1] * len(a)

for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            if a[i] < a[j]:
                rank[i] += 1

for r in range(len(a)):
    print("%4d 점 - : %4d 등"%(a[r],rank[r]))
