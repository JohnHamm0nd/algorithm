"""
369 게임 만들기
"""

def three_six_nine(number):
    #num_list = []
    for n in range(1, number + 1):
        if "3" in str(n) or "6" in str(n) or "9" in str(n):
            X_count = str(n).count("3")
            X_count += str(n).count("6")
            X_count += str(n).count("9")
            print("X" * X_count, end = " ")
            #num_list.append("X" * X_count)
        else:
            print(n, end = " ")
            #num_list.append(n)

    #print(num_list)
    
    
if __name__ == "__main__":
    number = int(input("n값을 입력하세요 : "))
    three_six_nine(number)
