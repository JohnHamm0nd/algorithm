"""
주식차트는 분,초,시,일 등의 가격 데이터를 O(open), H(high), L(low), C(close)를 가지고 봉 형태로 표시해 줍니다. 이를 candlesticks chart라고 합니다.
그러면, 주식의 거래데이터가 아래와 가티 주어질 때 ohlc를 만듭니다.

### 
실제 상황과 비슷하게 하기 위해서 아래 예제를 조금 바꾸어보았습니다. 조건이 바뀌기 전에 답을 주신 '상파'님의 양해를 먼저 구합니다.
###

예) 1분마다 open, high, low, close를 만듭니다.
분:초, 거래가격
1:02, 1100
1:20, 1170
1:59, 1090
2:30, 1030
2:31, 1110
2:42, 1150
2:55, 1210
2:56, 1190
3:02, 1120
3:09, 1100
4:15, 1090
4:20, 1080
4:55, 1050
4:56, 1020
4:57, 1000

[조건] 실제 주식 거래의 경우,, 분당 거래 회수가 10번, 100번, 1000번 등일 수 있으므로, high, low를 찾을 때 되도록 전체 데이터에서 찾지 않고,, 앞뒤 데이터를 비교하여 찾아주십시오.. 

답: 
open = [1100, 1030, 1120, 1090]
high = [1170, 1210, 1120, 1090]
low = [1090, 1030, 1100, 1000]
close = [1090, 1190, 1100, 1000]
"""

d_list = [['1:02', 1100],
                ['1:20', 1170],
                ['1:59', 1090],
                ['2:30', 1030],
                ['2:31', 1110],
                ['2:42', 1150],
                ['2:55', 1210],
                ['2:56', 1190],
                ['3:02', 1120],
                ['3:09', 1100],
                ['4:15', 1090],
                ['4:20', 1080],
                ['4:55', 1050],
                ['4:56', 1020],
                ['4:57', 1000]]

Open = []
High = []
Low = []
Close = []

o = ''
high = 0
low = 9999999999

for i in range(len(d_list)):
    if d_list[i][0][0] != o:
        Open.append(d_list[i][1])
        o = d_list[i][0][0]
        if i > 1:
            High.append(high)
            Low.append(low)
            high = 0
            low = 9999999999
        if d_list[i][1] > high:
            high = d_list[i][1]
        if d_list[i][1] < low:
            low = d_list[i][1]
        if i > 1:
            Close.append(d_list[i-1][1])
    else:
        if d_list[i][1] > high:
            high = d_list[i][1]
        if d_list[i][1] < low:
            low = d_list[i][1]
    if i == len(d_list)-1:
        Close.append(d_list[i][1])
        High.append(high)
        Low.append(low)

print(Open)
print(High)
print(Low)
print(Close)
