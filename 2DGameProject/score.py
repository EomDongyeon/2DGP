def score_check(num):      # 게임 스코어 및 게임 머니 체크
    Num = []
    temp_num = num
    count = 0

    while temp_num > 0:
        Num.append(int(temp_num % 10))
        temp_num = int(temp_num / 10)
        count += 1
    return Num
