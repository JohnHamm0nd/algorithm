"""
연구자의 연구업적을 평가할 때 사용되는 지표 중 h-index와 g-index라는 것이 있다.

h-index : 인용 횟수가 h번 이상인 논문이 h개일 때 가능한 h의 최댓값
g-index : 인용 횟수가 높은 상위 g개 논문의 인용 횟수 총합이 g²이상일 때 가능한 g의 최댓값
어떤 학자가 쓴 논문 각각의 인용 횟수가 주어질 때, h-index와 g-index를 계산하시오.

e.g.)
입력 : 0 15 4 0 7 10 0
h-index : 4
g-index : 6
"""

dissertations = list(map(int, input('입력: ').split()))
dissertations.sort(reverse=True)
for i in range(len(dissertations)):
    if dissertations[i] <= i+1:
        print('%s %d' %('h-index: ', dissertations[i]))
        break
g = sum(dissertations)
count = 0
g_index = 0
for i in range(len(dissertations)):
    count += 1
    if count * count <= g:
        g_index += 1
print('%s %d' %('g-index: ', g_index))
