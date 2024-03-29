"""
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.

    22220228 ==> 2222/02/28
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
[그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

        1월 1~31    2월 1~28    3월 1~31    4월 1~30
        5월 1~31    6월 1~30    7월 1~31    8월 1~31
        9월 1~30    10월 1~31   11월 1~30   12월 1~31
※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
5
22220228
20150002
01010101
20140230
11111111
출력
#1 2222/02/28
#2 -1
#3 0101/01/01
#4 -1
#5 1111/11/11
"""

import sys

sys.stdin = open('2056.txt', 'r', encoding = 'UTF-8')


T = int(input())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ymd = []
for t in range(T):
    date = input()
    y = date[:4]
    m = date[4:6]
    d = date[6:8]
    if y[0] != '0' and 0 < int(m) <= 12:
        if 1 <= int(d) <= day[int(m)-1]:
            ymd.append(y+"/"+m+"/"+d)
        else:
            ymd.append(-1)
    else:
        ymd.append(-1)

for idx, date in enumerate(ymd):
    print("#{idx} {date}".format(idx=idx+1, date=date))

"""
다른답안.(year check 안함)
n = int(input())
cal = {1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31}

for idx in range(n):
    date = input()
    year, month, day = date[:4], date[4:6], date[6:]
    if not (float(month) in cal.keys()) or not (float(day) in range(1, cal[float(month)]+1)):
        print(f'#{idx+1} -1')
    else:
        print(f'#{idx+1} {year}/{month}/{day}')
"""
