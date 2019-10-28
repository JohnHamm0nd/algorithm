"""
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
"""

S=(1, 3, 4, 8, 13, 17, 20)
distance = 99

for i in range(len(S)-1):
    if S[i+1] - S[i] < distance:
        distance = S[i+1] - S[i]
        result = (S[i], S[i+1])
print(result)


"""
# zip과 lambda 함수 사용
s= [1, 3, 4, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))
pairs.sort(key=lambda x:x[1]-x[0])
print(pairs[0])
"""
