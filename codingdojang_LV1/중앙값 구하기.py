"""
리스트에 있는 숫자들의 중앙값을 구하는 프로그램을 만들어라.
[7, 9, 14] = 9
[24, 31, 35, 49] = 33
[17, 37, 37, 47, 57] = 37
중앙값 : 자료를 작은 값에서부터 크기순으로 나열할 때 중앙에 위치한 값
① 자료의 개수가 홀수이면 가운데 위치한 값이 중앙값이다.
② 자료의 개수가 짝수이면 가운데 위치한 두 값의 평균이 중앙값이다.
"""

list_a = [7, 9, 14]
list_b = [24, 31, 35, 49]
list_c = [17, 37, 37, 47, 57]
list_d = [15, 16, 20, 21, 26, 50]

# 정렬 된 리스트라고 가정. (정렬된 리스트가 아니면 sort, sorted 함수 사용하여 정렬 후 계산)

def median(n_list):
    if len(n_list) % 2 == 1:
        return n_list[len(n_list)//2]
    else:
        return (n_list[(len(n_list)//2)-1] + n_list[(len(n_list)//2)]) / 2
        
print(median(list_a))
print(median(list_b))
print(median(list_c))
print(median(list_d))
