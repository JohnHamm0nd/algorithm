"""
개의 각으로 삼각형의 예각, 직각, 둔각을 구별하는 프로그램을 만들어라.
[60, 60, 60] = 예각삼각형
[30, 60, 90] = 직각삼각형
[20, 40, 120] = 둔각삼각형
[0, 90, 90] = 삼각형이 아니다
[60, 70, 80] = 삼각형이 아니다
[40, 40, 50, 50] = 삼각형이 아니다

예각삼각형 : 3개의 각이 모두 예각인 삼각형
직각삼각형 : 1개의 각이 직각인 삼각형
둔각삼각형 : 1개의 각이 둔각인 삼각형
① 각이 3개가 아닐 경우 삼각형이 아니다.
② 3개의 각의 합이 180°가 아닐 경우 삼각형이 아니다.
"""

def check_triangle(t_list):
    if len(t_list) != 3 or sum(t_list) != 180 or 0 in t_list:
        return t_list, ': 삼각형이 아니다.'
    elif 90 in t_list:
        return t_list, ': 직각삼각형.'
    elif t_list[0] > 90 or  t_list[1] > 90 or  t_list[2] > 90:
        return t_list, ': 둔각삼각형.'
    else:
        return t_list, ': 예각삼각형.'


triangle_list = [[60, 60, 60], [30, 60, 90], [20, 40, 120], [0, 90, 90], [60, 70, 80], [40, 40, 50, 50]]

for t_list in triangle_list:
    print(check_triangle(t_list))


"""
# 좀더 간략한 코드
def testTri(l1):
    if len(l1) != 3 or sum(l1) != 180 or min(l1) <= 0: return "삼각형이 아니다"
    if 90 in l1: return "직각삼각형"
    if max(l1) > 90: return "둔각삼각형"
    return "예각삼각형"

list1 = [[60, 60, 60],
    [30, 60, 90],
    [20, 40, 120],
    [0, 90, 90],
    [60, 70, 80],
    [40, 40, 50, 50]]


for l1 in list1:
    print(l1, '=', testTri(l1))
"""
