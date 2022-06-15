def solution(lottos, win_nums):
    count = 0
    cnt_0 = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        
    return [min(7 - (count + cnt_0), 6), min(7 - count, 6)]